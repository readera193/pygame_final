import socket
from _thread import *
import pickle
import json
from game import Game
from digital_punch_db import Digital_punch_DB

server = "127.0.0.1"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
db = Digital_punch_DB()

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, addr):
    global idCount
    opration_dict = json.loads(conn.recv(4096).decode())
    if opration_dict["action"] == "login":
        result = db.user_login(tuple(opration_dict["info"]))
        if result:
            conn.sendall(result.encode())
        else:
            conn.sendall("None".encode())
        conn.close()
        return

    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data[:3] == "add":
                        print(data[3:] + " won")
                        db.winner_add_score(data[3:])
                    elif data != "get":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()

if __name__ == "__main__":
    while True:
        conn, addr = s.accept()
        start_new_thread(threaded_client, (conn, addr))
