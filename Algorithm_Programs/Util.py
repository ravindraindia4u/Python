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

    # Function to find dayOfWeek
    @staticmethod
    def dayOfWeek(d, m, y):
        y0 = y - (14 - m) // 12
        x = y0 + (y0 // 4) - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + (31 * m0) // 12) % 7
        return d0

    # Function for temperature conversion
    @staticmethod
    def temperatureConversion(choice, temp):
        if choice == 1:
            cel_to_feh = round((temp * 9 / 5) + 32, 4)
            print("Temperature", temp, "C =", cel_to_feh, "F")
        elif choice == 2:
            feh_to_cel = round((temp - 32) * 5 / 9, 4)
            print("Temperature", temp, "F =", feh_to_cel, "C")
        else:
            print("Invalid Option...!!")

    # Function to calculate monthlyPayment
    @staticmethod
    def monthlyPayment(P, Y, R):
        n = 12 * Y
        r = R / (12 * 100)
        payment = (P * r) / (1 - (pow((1 + r), (-n))))
        return payment

    # Function to compute the square root of a nonnegative number
    @staticmethod
    def square_root(c):
        epsilon = float(1e-15)
        t = c
        while abs(t - c / t) > epsilon * t:
            t = float((c / t + t) / 2)
        return t

    # Function for Decimal to Binary Conversion
    @staticmethod
    def decimal_to_binary(num):
        if num > 1:
            Util.decimal_to_binary(num // 2)
        print(num % 2, end=" ")

    # Function for nibble swapping
    @staticmethod
    def nibble_Swap(num):
        return (num & 0x0F) << 4 | (num & 0xF0) >> 4


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
