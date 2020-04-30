"""
Add the Prime Numbers that are Anagram in the Range of 0 ­ 1000 in a Queue using
the Linked List and Print the Anagrams from the Queue. Note no Collection Library
can be used
"""
from Data_Structure_Programs.queue import Queue, Node
from Data_Structure_Programs.Prime_Number import Prime

obj = Queue()

# creating object of prime class
prime_obj = Prime()
# prime number list
prime_anagram = []
# creating prime number list in given range
prime_list = prime_obj.prime(0, 1000)
for num in prime_list:
    if num <= 10:
        continue
    number = prime_obj.anagram(num)
    if prime_obj.prime_check(number) and 0 <= number <= 1000:
        prime_anagram.append(number)
        prime_anagram.append(num)
        prime_list.remove(number)

# length of prime anagram list
length = len(prime_anagram)
# Adding the prime anagram into queue
for number in range(length):
    num = Node(prime_anagram[number])
    obj.enqueue(num)

# printing the prime anagram form Queue obj
obj.traverse()

