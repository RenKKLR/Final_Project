from tkinter import *
from tkinter import messagebox
import csv


print("Welcom to Trading Performance Query - Version2")
#save the entries in csv file buy.csv after click button Buy
def buy():
  #get entries from input box
  name = stockname.get().title()
  id = stockid.get()
  price = stockprice.get()
  amount = stockamount.get()
  date = stockdate.get()
  #delete entries after submit
  stockname.delete(0, END)
  stockid.delete(0, END)
  stockprice.delete(0, END)
  stockamount.delete(0, END)
  stockdate.delete(0, END)
  # save the entry in the file buy.csv
  stock = Stock(name, id)
  transaction = Transaction(stock, price,amount, date)
  transaction.save_transaction("buy.csv", transaction)


# do the sell_stock function after click button Sell
def sell():
  #get entries from input box
  name = stockname.get().title()
  id = stockid.get()
  price = stockprice.get()
  amount = stockamount.get()
  date = stockdate.get()
  #delete entries after submit
  stockname.delete(0, END)
  stockid.delete(0, END)
  stockprice.delete(0, END)
  stockamount.delete(0, END)
  stockdate.delete(0, END)
  # save the entry in the file sell.csv
  stock = Stock(name, id)
  transaction = Transaction(stock, price,amount, date)
  transaction.sell_stock("sell.csv", transaction)

#create a new window to do a single query
def create_window():
    def submit():
        sName_query = stockname_query.get().title()
        stockname_query.delete(0, END)
        Transaction.calculate_single_stock_performance(sName_query)

    # window design
    window = Tk()
    window.geometry("500x400")
    window.title("Redi Final Project")
    heading = Label(window, text="Single Stock Query", bg="grey", fg="black", width="500")
    heading.pack()

    # could close the main screen when the query window is opened
    # screen.destroy()

    # window definition and position of label, entry and button
    stockname_text = Label(window, text="Name of Stock *")
    stockname_text.place(x=15, y=50)
    stockname_query = Entry(window)
    stockname_query.place(x=15, y=80)

    submit_btn = Button(window, text="Submit", command=submit, bg="grey")
    submit_btn.place(x=15, y=150)

    window.mainloop()



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
            print(f"Stock {transaction.stock.name} in {transaction.amount} share(s) has been saved in {filename} successfully!")

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

        if remaining_stock - int(amount_to_sell) >= 0:
            with open("sell.csv", "a", newline="") as file:
                file.write(f"{sell_transaction.stock.name};"
                           f"{sell_transaction.stock.stock_id};"
                           f"{sell_transaction.price};"
                           f"{sell_transaction.amount};"
                           f"{sell_transaction.date}\n")
                print(f"Stock {stock_name} in {sell_transaction.amount} share(s) has been saved in sell.csv successfully.")
        else:
            print(f"You don't have enough stock {stock_name} to sell {amount_to_sell} share(s).")


    @staticmethod
    def calculate_single_stock_performance(stock_name):
        bought_amount = 0
        sold_amount = 0

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
                else:
                    sold_value = 0


        if bought_amount == 0:
            print(f"You haven't bought stock {stock_name} yet.")


        elif bought_amount > sold_amount:
            current_price = float(input("Please enter the current selling price: "))
            remaining_shares = bought_amount - sold_amount
            current_value = current_price * remaining_shares

            single_stock_performance = performance(sold_value+current_value, bought_value)
            print(f"Current value of unsold stock {stock_name}: €{current_value:.2f}")
            print(f"Sold value of stock {stock_name}: €{sold_value:.2f}")
            print(f"Bought value of stock {stock_name}: €{bought_value:.2f}")
            print(f"Current performance of stock {stock_name}: {single_stock_performance:+.2f}%")

        else:
            single_stock_performance = performance(sold_value, bought_value)
            bought_value = bought_amount * float(buy_transaction[2])
            print(f"Bought value of stock {stock_name}: €{bought_value:.2f}")
            print(f"Sold value of stock {stock_name}: €{sold_value:.2f}")
            print(f"Performance of stock {stock_name}: {single_stock_performance:+.2f}%")


#screen design
screen = Tk()
screen.geometry("500x500")
screen.title("ReDi Final Project")
heading = Label(text="Trading Performance Query - Version2", bg="grey", fg="black", width="500")
heading.pack()

#screen label definition and positon
stockname_text = Label(text = "Name of Stock *")
stockid_text = Label(text = "Stock ID (WKN / ISIN) ")
stockprice_text = Label(text = "Price per Share (in Euro) *")
stockamount_text = Label(text = "Amount *")
stockdate_text = Label(text = "Date of Transaction (YYYY-MM-DD) *")
stockname_text.place(x = 15, y = 70)
stockid_text.place(x = 270, y = 70)
stockprice_text.place(x = 15, y = 140)
stockamount_text.place(x = 270, y = 140)
stockdate_text.place(x = 15, y = 210)

#screen entry definition and position
stockname = Entry()
stockid = Entry()
stockprice = Entry()
stockamount = Entry()
stockdate = Entry()
stockname.place(x = 15, y = 100)
stockid.place(x = 270, y = 100)
stockprice.place(x = 15, y = 170)
stockamount.place(x = 270, y = 170)
stockdate.place(x = 15, y = 240)

#screen button to buy or sell or do a single stock query
buy_btn = Button(screen, text ="Buy", command=buy, bg = "grey")
sell_btn = Button(screen, text = "Sell", command=sell, bg ="grey")
query_btn = Button(screen, text="Single Stock Query", command=create_window, bg="grey")
buy_btn.place(x = 15, y = 290)
sell_btn.place(x = 65, y = 290)
query_btn.place(x=15, y=333)

screen.mainloop()





#stock = Stock("Microsoft", "54321")
#price = 270
#amount = 20
#date = "2023-11-20"



#transaction = Transaction(stock, price, amount, date)

#transaction.save_transaction("buy.csv", transaction)
#transaction.sell_stock("buy.csv", transaction)
#Transaction.calculate_single_stock_performance("Microsoft")


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



