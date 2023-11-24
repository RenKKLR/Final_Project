from tkinter import *
from app import Transaction
from app import Stock

print("Welcome to Trading Performance Query - Version2")


# save the entries in csv file buy.csv after click button Buy
def buy():
    # get entries from input box
    name = stockname.get().title()
    id = stockid.get()
    price = stockprice.get()
    amount = stockamount.get()
    date = stockdate.get()
    # delete entries after submit
    stockname.delete(0, END)
    stockid.delete(0, END)
    stockprice.delete(0, END)
    stockamount.delete(0, END)
    stockdate.delete(0, END)
    # save the entry in the file buy.csv
    stock = Stock(name, id)
    transaction = Transaction(stock, price, amount, date)
    transaction.save_transaction("buy.csv", transaction)


# do the sell_stock function after click button Sell
def sell():
    # get entries from input box
    name = stockname.get().title()
    id = stockid.get()
    price = stockprice.get()
    amount = stockamount.get()
    date = stockdate.get()
    # delete entries after submit
    stockname.delete(0, END)
    stockid.delete(0, END)
    stockprice.delete(0, END)
    stockamount.delete(0, END)
    stockdate.delete(0, END)
    # save the entry in the file sell.csv
    stock = Stock(name, id)
    transaction = Transaction(stock, price, amount, date)
    transaction.sell_stock("sell.csv", transaction)


# create a new window to do a single query
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


# screen design
screen = Tk()
screen.geometry("500x500")
screen.title("ReDi Final Project")
heading = Label(text="Trading Performance Query - Version2", bg="grey", fg="black", width="500")
heading.pack()

# screen label definition and positon
stockname_text = Label(text="Name of Stock *")
stockid_text = Label(text="Stock ID (WKN / ISIN) ")
stockprice_text = Label(text="Price per Share (in Euro) *")
stockamount_text = Label(text="Amount *")
stockdate_text = Label(text="Date of Transaction (YYYY-MM-DD) *")
stockname_text.place(x=15, y=70)
stockid_text.place(x=270, y=70)
stockprice_text.place(x=15, y=140)
stockamount_text.place(x=270, y=140)
stockdate_text.place(x=15, y=210)

# screen entry definition and position
stockname = Entry()
stockid = Entry()
stockprice = Entry()
stockamount = Entry()
stockdate = Entry()
stockname.place(x=15, y=100)
stockid.place(x=270, y=100)
stockprice.place(x=15, y=170)
stockamount.place(x=270, y=170)
stockdate.place(x=15, y=240)

# screen button to buy or sell or do a single stock query
buy_btn = Button(screen, text="Buy", command=buy, bg="grey")
sell_btn = Button(screen, text="Sell", command=sell, bg="grey")
query_btn = Button(screen, text="Single Stock Query", command=create_window, bg="grey")
buy_btn.place(x=15, y=290)
sell_btn.place(x=65, y=290)
query_btn.place(x=15, y=333)

screen.mainloop()
