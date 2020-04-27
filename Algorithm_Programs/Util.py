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
        list = []
        for i in range(start, end):
            if i == 1 or i == 0:
                continue
            count = 0
            for j in range(2, i):
                if i % j == 0:
                    count += 1
            if count == 0 and i != 1:
                print(i, end=" ")
