# network.py
import socket
import pickle, json
 
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 5555
        self.addr = (self.server, self.port)
 
    # {"action":"login", "info":(<user_id>, <password>)} return user_id
    # {"action":"getPlayer"} return player
    def connect(self, opration_dict):
        try:
            self.client.connect(self.addr)
            self.client.send(json.dumps(opration_dict).encode())
            return self.client.recv(2048).decode()
        except:
            pass
 
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)

