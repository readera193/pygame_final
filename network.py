# network.py
import socket
import pickle, json
from dotenv import load_dotenv
import os

load_dotenv()
 
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = os.getenv("SERVER")
        self.port = int(os.getenv("PORT"))
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

