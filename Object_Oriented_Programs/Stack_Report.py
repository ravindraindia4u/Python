"""
Write a program to read in Stock Names, Number of Share, Share Price.
Print a Stock Report with total value of each Stock and the total value of Stock.
"""


class Stocks:
    def __init__(self, name, number, price):
        self.name = name
        self.number = number
        self.price = price


class Portfolio:
    def __init__(self):
        self.value = 0
        self.portfolio = []

    # Function to add new Stock into the portfolio list
    def addStock(self, name, number, price):
        new_Stock = Stocks(name, number, price)
        self.portfolio.append(new_Stock)

    def portfolio_details(self):
        for obj in self.portfolio:
            print(f"{obj.name}:\n\tPrice per share: {obj.price}\n\tNumber of Shares: {obj.number}\n\tValue: {obj.price * obj.number}")

    def total_portfolio_value(self):
        for obj in self.portfolio:
            self.value += obj.number * obj.price


portfolio_obj = Portfolio()
portfolio_obj.addStock("Reliance", 210, 10000)
portfolio_obj.addStock("Nippon", 114, 200000)
portfolio_obj.addStock("Bajaj", 540, 50000)
portfolio_obj.portfolio_details()
portfolio_obj.total_portfolio_value()
print("Total Portfolio value =", portfolio_obj.value)