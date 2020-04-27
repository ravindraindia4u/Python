from Algorithm_Programs.Util import Util

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if Util.anagram(string1, string2):
    print(string1, "and", string2, "are anagram.")
else:
    print(string1, "and", string2, "are not anagram.")