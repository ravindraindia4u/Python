class Util:
    # Function to check anagram or not
    @staticmethod
    def anagram(string1, string2):
        if sorted(string1) == sorted(string2):
            return True
        else:
            return False