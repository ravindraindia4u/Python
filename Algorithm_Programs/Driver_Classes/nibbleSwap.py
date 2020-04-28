from Algorithm_Programs.Util import Util

num = int(input("Enter a number: "))
print("Binary digit of number", num, "is :", end=" ")
Util.decimal_to_binary(num)
print("\nAfter swap two nibbles, The Decimal Number is :", Util.nibble_Swap(num))
