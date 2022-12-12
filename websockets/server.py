import socket
import threading
import json
from enum import Enum



HEADER_SIZE = 64
PORT = 5000
SERVER_IP = socket.gethostbyname(socket.gethostname())
# needs to be a tuple
ADDRESS = (SERVER_IP, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

stocks = [
  {"id": 1, "name": "apple", "price": 12, "quantity": 1},
  {"id": 2, "name": "google", "price": 22, "quantity": 2},
]

purchase_history = []

class Endpoints(str, Enum):
  STOCKS = "/stocks"
  BUYSTOCKS = "/stocks/buy"

schema = {
    Endpoints.STOCKS: stocks,
    Endpoints.BUYSTOCKS: purchase_history
}

def handle_responses(msg):
    request = json.loads(msg)
    if type(request) is dict:
        endpoint = request.get("endpoint")
        payload = request.get("payload")
        if payload:
            if request["endpoint"] == Endpoints.BUYSTOCKS:
                purchase_history.append(payload)
        data = schema[endpoint]
        return json.dumps(data)
    return ""

def handle_client(conn, addr):
    print(f"new connection: {addr} connected")

    connected = True

    while connected:
        msg_length = conn.recv(HEADER_SIZE).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            response = "{}"
            if msg == DISCONNECT_MESSAGE:
                connected = False
            else:
                response = handle_responses(msg)

            conn.send(f"{response}".encode(FORMAT))
    
    conn.close()


def start():
    server.listen()
    print(f"Server is listening on http://{SERVER_IP}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"active connections {threading.activeCount() - 1}")

print("starting server...")
start()