class Util:
    # Function to check anagram or not
    @staticmethod
    def anagram(string1, string2):
        if sorted(string1) == sorted(string2):
            return True
        else:
            return False

    # Function to find prime number in given range
    @staticmethod
    def prime(start, end):
        for i in range(start, end):
            if i == 1 or i == 0:
                continue
            count = 0
            for j in range(2, i):
                if i % j == 0:
                    count += 1
            if count == 0 and i != 1:
                print(i, end=" ")

    # Function for palindrome number
    @staticmethod
    def palindrome(num):
        temp = num
        rev = 0
        while num > 0:
            dig = num % 10
            rev = rev * 10 + dig
            num //= 10
        if temp == rev:
            return True
        else:
            return False

    # Function to find the prime numbers that are Anagram and Palindrome
    @staticmethod
    def primeAndPalindrome(start, end):
        start = int(start)
        end = int(end)
        prime_list = []
        palindrome_list = []
        for i in range(start, end):
            if i == 1 or i == 0:
                continue
            count = 0
            for j in range(2, i):
                if i % j == 0:
                    count += 1
            if count == 0 and i != 1:
                prime_list.append(i)
        for i in range(0, len(prime_list)):
            if palindrome(prime_list[i]):
                palindrome_list.append(prime_list[i])
        return palindrome_list
        print(palindrome_list)


def palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num //= 10
    if temp == rev:
        return True
    else:
        return False
        pass
