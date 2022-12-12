import socket
import json

HEADER_SIZE = 64
HEADER_SIZE_2 = 2048
PORT = 5000
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER_IP = "192.168.10.112"
ADDRESS = (SERVER_IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER_SIZE - len(send_length))
    client.send(send_length)
    client.send(message)
    return client.recv(HEADER_SIZE_2).decode(FORMAT)


def get_stocks():
    payload = json.dumps({ "endpoint": "/stocks" })
    response = send(payload)
    return response

def buy_stock(id, price, quantity):
    obj = {
      "id": id,
      "price": price,
      "quantity": quantity
    }

    payload = json.dumps({ "endpoint": "/stocks/buy", "payload": obj})
    response = send(payload)
    return response


print(get_stocks())
print(buy_stock(1, 2, 10))
send(DISCONNECT_MESSAGE)