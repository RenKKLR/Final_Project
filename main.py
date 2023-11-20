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
            print(f"Stock {stock.name} in {amount} share(s) has been saved in {filename} successfully!")

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

        bought_amount = Transaction.single_stock_count("buy.csv", stock_name)
        sold_amount = Transaction.single_stock_count("sell.csv", stock_name)

        remaining_stock = bought_amount - sold_amount

        if remaining_stock >= amount_to_sell:
            with open("sell.csv", "a", newline="") as file:
                file.write(f"{sell_transaction.stock.name};"
                           f"{sell_transaction.stock.stock_id};"
                           f"{sell_transaction.price};"
                           f"{sell_transaction.amount};"
                           f"{sell_transaction.date}\n")
                print(f"Stock {stock_name} in {amount} share(s) has been saved in sell.csv successfully.")
        else:
            print(f"You don't have enough stock {stock_name} to sell {amount_to_sell} share(s).")


    @staticmethod
    def calculate_single_stock_performance(stock_name):
        bought_amount = 0
        sold_amount = 0
       #buy_transactions = []
        #sell_transactions = []
        def performance(sell_sum, buy_sum):
            return (sell_sum -buy_sum) / buy_sum * 100

        with open("buy.csv") as buy_file:
            buy_transactions = csv.reader(buy_file, delimiter=";")
            for buy_transaction in buy_transactions:
                if stock_name == buy_transaction[0]:
                    bought_amount += int(buy_transaction[3])
                    bought_value = bought_amount * float(buy_transaction[2])
                    print("Bought: ", buy_transaction)


        with open("sell.csv") as sell_file:
            sell_transactions = csv.reader(sell_file, delimiter=";")
            for sell_transaction in sell_transactions:
                if stock_name == sell_transaction[0]:
                    sold_amount += int(sell_transaction[3])
                    sold_value = sold_amount * float(sell_transaction[2])
                    print("Sold: ", sell_transaction)

        if bought_amount == 0:
            print(f"You haven't bought stock {stock_name} yet.")

        elif bought_amount > sold_amount:
            current_price = float(input("Please enter the current selling price: "))
            remaining_shares = bought_amount - sold_amount
            current_value = current_price * remaining_shares
            single_stock_performance = performance(sold_value+current_value, bought_value)
            print(f"Current value of stock {stock_name}: €{current_value:.2f}")
            print(f"Bought value of stock {stock_name}: €{bought_value:.2f}")
            print(f"Sold value of stock {stock_name}: €{sold_value:.2f}")
            print(f"Performance of stock {stock_name}: {single_stock_performance:+.2f}%")

        else:
            single_stock_performance = performance(sold_value, bought_value)
            print(f"Bought value of stock {stock_name}: €{bought_value:.2f}")
            print(f"Sold value of stock {stock_name}: €{sold_value:.2f}")
            print(f"Performance of stock {stock_name}: {single_stock_performance:+.2f}%")








stock = Stock("Amazon", "12345")
price = 75
amount = 290
date = "2023-11-20"

transaction = Transaction(stock, price, amount, date)

#transaction.save_transaction("buy.csv", transaction)
transaction.sell_stock("buy.csv", transaction)
#transaction.calculate_single_stock_performance("Amazon")


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



