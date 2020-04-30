# Function to check number is prime or not
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

        # This is checked so that we can skip
        # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


class Prime:
    def __init__(self):
        self.list = []

    # Function for prime number in given range
    def prime(self, range1, range2):
        arr = []
        for num in range(range1, range2 + 1):
            if Prime.prime_check(self, num):
                arr.append(num)
        self.list.append(arr)
        return arr

    # Function to print 2D array
    def Print(self, itr):
        for num in range(itr):
            print(self.list[num])

    # Function to check anagram number
    def anagram(self, num):
        temp = 0
        while num >= 10:
            temp = (temp * 10) + (num % 10)
            num = num // 10
        temp = (temp * 10) + (num % 10)
        return temp

    def prime_check(self, num):
        if num < 2:
            return False
        count = 0
        for number in range(2, (num // 2) + 1):
            if num % number == 0:
                count += 1
                return False
        if count == 0:
            return True

    def PrintList(self, array):
        count = 0
        for i in range(0, len(array)):
            if count < 15:
                if array[i] < 10:
                    print(f"  {array[i]}", end=" ")
                elif array[i] < 100:
                    print(f" {array[i]}", end=" ")
                else:
                    print(array[i], end=" ")
                count += 1
            if count == 15:
                print()
                count = 0
