import trades_pb2_grpc
import trades_pb2
import grpc


def getStock(stockName):
    stub = trades_pb2_grpc.TradesStub(channel)
    request = trades_pb2.SelectStock(name=stockName)
    response = stub.getStock(request)
    print("#############gettingStock################")

def getStockStream(stockName):
    stub = trades_pb2_grpc.TradesStub(channel)
    request = trades_pb2.SelectStock(name=stockName)
    responses = stub.getStockStream(request)

    for response in responses:
        print(response)
        if response.price == 12:
            buyStock(response.id, response.price, response.quantity, response.name)

def getStocks():
    stub = trades_pb2_grpc.TradesStub(channel)
    request = trades_pb2.Void()
    response = stub.getStocks(request)
    print(response.stocks)


def buyStock(id, price, quantity, stockName):
    stub = trades_pb2_grpc.TradesStub(channel)
    request = trades_pb2.Stock(id=id, price=price, quantity=quantity, name=stockName)
    response = stub.buyStock(request)
    print(response.purchasehistory)


with grpc.insecure_channel("localhost:5000") as channel:
    getStock("GOOL")
    getStockStream("GOOL")
    # getStocks()
    # buyStock(1, 10, 5)