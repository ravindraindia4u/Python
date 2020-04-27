from Algorithm_Programs.Util import Util

start = input("Enter starting Range: ")
end = input("Enter ending Range: ")
print("Palindrome number between", start, "to", end, "are:", end=" ")
print(Util.primeAndPalindrome(start, end))
