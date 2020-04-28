from Algorithm_Programs.Util import Util

p_amount = int(input("Enter the principal amount: "))
year = int(input("Enter how many year you take to repayment: "))
rate = int(input("Enter the rate of interest: "))
monthlyPayment = Util.monthlyPayment(p_amount, year, rate)
print("monthly payments you would have to make over", year, "years is Rs:", round(monthlyPayment, 2))