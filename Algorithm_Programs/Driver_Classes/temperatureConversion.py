from Algorithm_Programs.Util import Util

choice = int(input("Choose Option: \n 1. Celsius to Fahrenheit: \n 2. Fahrenheit to Celsius:"))
temp = int(input("Enter temperature for conversion: "))
Util.temperatureConversion(choice, temp)