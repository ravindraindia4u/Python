"""
A palindrome is a string that reads the same forward and backward, for
example, radar, toot, and madam. We would like to construct an algorithm to
input a string of characters and check whether it is a palindrome.
"""
from Data_Structure_Programs.dequeue import Dequeue, Node

obj = Dequeue()
string = input("Enter a string of characters to check whether it is a palindrome or not: ")


def isPalindrome(string):
    for character in string:
        ch = Node(character)
        obj.addFront(ch)

    length = obj.size()
    string2 = ""
    for len in range(length):
        ch = obj.removeFront()
        string2 += ch

    if string == string2:
        print("String is Palindrome!!")
    else:
        print("String is not Palindrome!!")


isPalindrome(string)
