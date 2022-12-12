import asyncio
import websockets
import json
from enum import Enum

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

## for client2.py
# def handle_responses(msg):
#     request = json.loads(msg)
#     print(request)
#     if type(request) is dict:
#         endpoint = request.get("endpoint")
#         payload = request.get("payload")
#         if payload:
#             if request["endpoint"] == Endpoints.BUYSTOCKS:
#                 purchase_history.append(payload)
#         data = schema[endpoint]
#         return json.dumps(data)
#     return ""

# async def handle_client(websocket):
#     request_str = await websocket.recv()
#     response = handle_responses(request_str)
#     await websocket.send(response)


## for client3.py
async def handle_responses(msg, ws):
    import time
    from random import randrange

    request = json.loads(msg)
    print("request", request)
    if type(request) is dict:
        action = request.get("action")
        if action == "auth":
            if request.get("params") == "API KEY":
                return "authenticated"
        elif action == "subscribe":
            if request.get("params") == "APPL":
                while True:
                    response = json.dumps(
                      {"id": 1, "name": "apple", "price": randrange(20), "quantity": randrange(10)},
                    )
                    time.sleep(1)
                    await ws.send(response)
                    request_str = await ws.recv()
                    print(request_str)
    return ""



async def handle_client(websocket):
    request_str = await websocket.recv()
    response = await handle_responses(request_str, websocket)
    await websocket.send(response)

async def main():
    async with websockets.serve(handle_client, "localhost", 5000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())