from concurrent import futures
import grpc
import trades_pb2
import trades_pb2_grpc
import time
from random import randrange
        

stocks = [
  {"id": 1, "name": "apple", "price": 12, "quantity": 1},
  {"id": 2, "name": "google", "price": 22, "quantity": 2},
]

stocksNames = {
    "APPL": "APPL",
    "GOOL": "GOOL"
}

purchase_history = []

class TradesServicer(trades_pb2_grpc.TradesServicer):
    def getStock(self, request, context):
        stock = trades_pb2.Stock()
        stock.id = 1
        stock.price = randrange(20)
        stock.quantity = randrange(10)
        stock.name = stocksNames[request.name]

        return stock

    def getStockStream(self, request, context):
        while True:
            stock = trades_pb2.Stock()
            stock.id = 1
            stock.price = randrange(20)
            stock.quantity = randrange(10)
            stock.name = stocksNames[request.name]
            time.sleep(1)
            yield stock

    def getStocks(self, request, context):
        response = trades_pb2.Stocks()
        for stock in stocks:
            current_stock = trades_pb2.Stock()
            for key, value in stock.items():
                setattr(current_stock, key, value)
            # current_stock.id = stock["id"]
            # current_stock.price = stock["price"]
            # current_stock.quantity = stock["quantity"]
            # current_stock.name = stock["name"]
            response.stocks.append(current_stock)

        return response

    def buyStock(self, request, context):
        print("buyStock", request, context)
        response = trades_pb2.PurchaseHistory()
        stock = trades_pb2.Stock()
        stock.id = request.id
        stock.price = request.price
        stock.quantity = request.quantity
        stock.name = request.name
        purchase_history.append(stock)
        response.purchasehistory.extend(purchase_history)

        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    trades_pb2_grpc.add_TradesServicer_to_server(TradesServicer(), server)
    server.add_insecure_port("localhost:5000")
    server.start()
    server.wait_for_termination()

  
if __name__ == "__main__":
    serve()