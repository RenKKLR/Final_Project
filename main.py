import csv


class Stock:
    def __init__(self, name, stock_id):
        self.name = name
        self.stock_id = stock_id


class Transaction:
    def __init__(self, stock, price, amount, date):
        self.stock = stock
        self.price = price
        self.amount = amount
        self.date = date

    @staticmethod
    def save_transaction(filename, transaction):
        with open(filename, "a", newline="") as file:
            file.write(f"{transaction.stock.name};"
                       f"{transaction.stock.stock_id};"
                       f"{transaction.price};"
                       f"{transaction.amount};"
                       f"{transaction.date}\n")

    @staticmethod
    def single_stock_count(filename, stock_name):
        single_stock_count = 0
        with open(filename) as transaction_file:
            transactions = csv.reader(transaction_file, delimiter=";")
            next(transactions)
            for transaction in transactions:
                if stock_name == transaction[0]:
                    single_stock_count += int(transaction[3])
        return single_stock_count

    @staticmethod
    def single_stock_sum(filename, stock_name):
        single_stock_sum = 0
        with open(filename) as transaction_file:
            transactions = csv.reader(transaction_file, delimiter=";")
            next(transactions)
            for transaction in transactions:
                if stock_name == transaction[0]:
                    single_stock_sum += (int(transaction[3]) * float(transaction[2]))
        return single_stock_sum

    @staticmethod
    def sell_stock(filename, sell_transaction):
        stock_name = sell_transaction.stock.name
        amount_to_sell = sell_transaction.amount

        remaining_stock = Transaction.single_stock_count(filename, stock_name)

        if remaining_stock >= amount_to_sell:
            with open(filename, "a", newline="") as file:
                file.write(f"{sell_transaction.stock.name};"
                           f"{sell_transaction.stock.stock_id};"
                           f"{sell_transaction.price};"
                           f"{-sell_transaction.amount};"
                           f"{sell_transaction.date}\n")
        else:
            print(f"You don't have enough stock {stock_name} to sell {amount_to_sell} share(s).")


stock = Stock("Amazon", "12345")
price = 55
amount = 380
date = "2023-11-20"

transaction = Transaction(stock, price, amount, date)

transaction.sell_stock("transaction.csv", transaction)

'''def main():

    stock = Stock("Amazon", "12345")
    price = 50
    amount = 100
    date = "2023-11-19"

    transaction = Transaction(stock, price, amount, date)

    transaction.save_transaction("transaction.csv", transaction)

    print(Transaction.single_stock_count("transaction.csv", "Amazon"))
    print(Transaction.single_stock_sum("transaction.csv", "Amazon"))


if __name__ == "__main__":
    main()'''



