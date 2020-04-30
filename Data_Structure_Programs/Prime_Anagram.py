"""
Prime Number Program and store only the numbers in that range that are Anagrams.
For e.g. 17 and 71 are both Prime and Anagrams in the 0 to 1000 range.
Further store in a 2D Array the numbers that are Anagram and numbers that are not Anagram
"""
from Data_Structure_Programs.Prime_Number import Prime

obj = Prime()

anagram_list = []

non_anagram = []

prime_list = obj.prime(0, 1000)

"""Checking the prime numbers are anagram or not"""
for num in prime_list:
    if num <= 10:
        non_anagram.append(num)
        continue
    number = obj.anagram(num)
    if obj.prime_check(number) and 0 <= number <= 1000:
        anagram_list.append(num)
        anagram_list.append(number)
    else:
        non_anagram.append(num)


print("Anagram prime numbers array----> ")
obj.PrintList(anagram_list)
print("\nNon anagram prime numbers array ----> ")
obj.PrintList(non_anagram)
