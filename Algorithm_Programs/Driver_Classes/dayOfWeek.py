from Algorithm_Programs.Util import Util

date = int(input("Enter the date: "))
month = int(input("Enter the month in the form of 1-12: "))
year = int(input("Enter the year: "))
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print("Day of the Week is :", days[Util.dayOfWeek(date, month, year)])