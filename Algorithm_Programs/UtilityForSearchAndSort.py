class Utility:
    @staticmethod
    def arrayList(array):
        number = int(input("How many element you want to add ? "))
        print("Enter", number, "Elements: ")
        for i in range(number):
            array.append(int(input()))
        return array

    # Function for Printing Array elements
    @staticmethod
    def printArray(array):
        print("Sorted list is :", end=" ")
        for i in range(0, len(array)):
            print(array[i], end=" ")

    # binarySearch method for integer
    @staticmethod
    def binarySearch(array, low, high, num):
        if high >= low:
            mid = int((low + high) / 2)
            if array[mid] == num:
                return mid
            elif array[mid] > num:
                return Utility.binarySearch(array, low, mid - 1, num)
            else:
                return Utility.binarySearch(array, mid + 1, high, num)
        else:
            return -1

    # insertionSort method for integer
    @staticmethod
    def insertionSort(array):
        for i in range(len(array)):
            temp = array[i]
            j = i - 1
            while j >= 0 and temp < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = temp
        return array

    # bubbleSort method for integer
    @staticmethod
    def bubbleSort(array):
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] > array[j]:
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
        return array

    # mergeSort method for String
    @staticmethod
    def mergeSort(array):
        k = 0
        if len(array) > 1:
            mid = int(len(array) / 2)
            left = array[:mid]
            right = array[mid:]
            Utility.mergeSort(left)
            Utility.mergeSort(right)
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                    k += 1
                else:
                    array[k] = right[j]
                    j += 1
                    k += 1
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
                return array


# main function
def main():
    choiceNo = int(input("Enter the choice: \n 1. Binary Search for integer: \n 2. Binary Search for string: \n 3. "
                         "Insertion Sort for Integer: \n 4. Insertion sort for String: \n 5. Bubble Sort for Integer: "
                         "\n 6. Bubble Sort for String: \n 7. Merge Sort for String: "))
    # Binary search calling for integer
    if choiceNo == 1:
        array = []
        array = Utility.arrayList(array)
        length = len(array)
        num = int(input("Enter the number to search in the list: "))
        result = int(Utility.binarySearch(array, 0, length, num))
        if result == -1:
            print("Element", num, "is not found in the list")
        else:
            print("Element", num, "is found in the list at index no:", result)
    # Binary Search calling for String
    elif choiceNo == 2:
        array = []
        number = int(input("How many elements you want to add ? "))
        print("Enter", number, "elements: ")
        for i in range(number):
            array.append(input())
        length = len(array)
        search = input("Enter element to search in the list: ")
        result = Utility.binarySearch(array, 0, length, search)
        if result != -1:
            print("Element", search, "is found in the list at index no:", result)
        else:
            print("Element", search, "is not found in the list")
    # Insertion sort for integer
    elif choiceNo == 3:
        array = []
        array = Utility.arrayList(array)
        array = Utility.insertionSort(array)
        Utility.printArray(array)

    # Insertion sort calling for string
    elif choiceNo == 4:
        array = []
        number = int(input("Enter how many elements you want to add: "))
        print("Enter", number, "elements: ")
        for i in range(number):
            array.append(input())
        array = Utility.insertionSort(array)
        Utility.printArray(array)
    # Sort the Integer element using bubble sort
    elif choiceNo == 5:
        array = []
        array = Utility.arrayList(array)
        array = Utility.bubbleSort(array)
        Utility.printArray(array)
    # Sort the String elements using bubble sort
    elif choiceNo == 6:
        array = []
        number = int(input("Enter how many element you want to insert: "))
        print("Enter", number, "elements: ")
        for i in range(number):
            array.append(input())
        array = Utility.bubbleSort(array)
        Utility.printArray(array)
    # Sort the String using merge sort
    elif choiceNo == 7:
        array = []
        number = int(input("Enter how many element you want to insert: "))
        print("Enter", number, "elements: ")
        for i in range(number):
            array.append(input())
        array = Utility.mergeSort(array)
        Utility.printArray(array)


# main function call
main()
