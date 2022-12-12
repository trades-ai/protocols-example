from flask import Flask, json, request

stocks = [
  {"id": 1, "name": "apple", "price": 12, "quantity": 1},
  {"id": 2, "name": "google", "price": 22, "quantity": 2},
]

purchase_history = []

api = Flask(__name__)

@api.route('/stocks', methods=['GET'])
def get_stocks():
  return json.dumps(stocks)

@api.route('/stocks/buy/<id>', methods=['POST'])
def buy_stock(id):
  data = request.get_json()
  data["id"] = id
  purchase_history.append(data)
  return purchase_history

if __name__ == '__main__':
    api.run()