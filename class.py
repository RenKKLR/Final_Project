import uuid


class Stock:
    def __init__(self, stock_name, stock_id):
        self.stock_name = stock_name
        self.stock_id = stock_id
        self.stock_list = []


class Transaction:
    def __init__(self, stock_name, stock_id, price, amount, date):
        self.obj_stock = Stock(stock_name, stock_id)
        self.price = price
        self.amount = amount
        self.date = date
        self.trans_id = str(uuid.uuid4())

    def buy(self, amount):
        self.amount += amount

    def sell(self, amount):
        self.amount -= amount



