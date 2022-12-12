import asyncio
import websockets
import json

uri = "ws://localhost:5000"

async def get_stocks():
    async with websockets.connect(uri) as websocket:
        request = json.dumps({ "endpoint": "/stocks" })

        await websocket.send(request)

        response_str = await websocket.recv()
        print(json.loads(response_str))

async def buy_stock(id, price, quantity):
    async with websockets.connect(uri) as websocket:
        obj = {
          "id": id,
          "price": price,
          "quantity": quantity
        }

        request = json.dumps({ "endpoint": "/stocks/buy", "payload": obj})

        await websocket.send(request)

        response_str = await websocket.recv()
        print(json.loads(response_str))

if __name__ == "__main__":
    asyncio.run(get_stocks())
    asyncio.run(buy_stock(1, 2, 10))