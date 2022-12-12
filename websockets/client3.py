import websocket, json

def on_open(ws):
    print("opened")
    auth_data = {
        "action": "auth",
        "params": "API KEY"
    }

    # ws.send(json.dumps(auth_data))

    channel_data = {
        "action": "subscribe",
        "params": "APPL"
    }

    ws.send(json.dumps(channel_data))


def on_message(ws, message):
    print("received a message")
    print(message)
    response = json.loads(message)

    obj = {
      "id": 1,
      "price": response.get("price"),
      "quantity": 1
    }
    if response.get("price") == 10:
        ws.send(json.dumps({ "action": "buy", "params": obj }))
    elif response.get("price") >= 18:
        ws.send(json.dumps({ "action": "sell", "params": obj }))
    ws.send("")

def on_close(ws):
    print("closed connection")

socket = "ws://localhost:5000"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()
