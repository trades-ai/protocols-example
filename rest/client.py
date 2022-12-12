import requests

url = "http://127.0.0.1:5000"

def get_stocks():
    response = requests.get(f"{url}/stocks")
    return response.json()


def buy_stock(id, price, quantity):
    obj = {
      "price": price,
      "quantity": quantity
    }
    response = requests.post(f"{url}/stocks/buy/{id}", json=obj)
    return response.json()


stocks = get_stocks()
purchase_history = buy_stock(1, 2, 10)

print(stocks)
print(purchase_history)