"""-----------------------LinkedList Implementation------------------------"""


# Creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Function for inserting element at the start
    def insert_start(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    # Function for inserting element at a position
    def insetAtIndex(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            position = int(input("Enter the position, Where you want to insert element: "))
            while True:
                if position > LinkedList.len(self):
                    print("You entered wrong position: ")
                    position = int(input("Enter the position, Where you want to insert element: "))
                else:
                    number = 1
                    lastNode = self.head
                    llastNode = lastNode.next
                    if position == 1:
                        LinkedList.insert_start(self, newNode)
                        break
                    else:
                        while number < position - 1:
                            lastNode = lastNode.next
                            llastNode = lastNode.next
                            number += 1
                        newNode.next = llastNode
                        lastNode.next = newNode
                        break

    # Function for inserting element at the end
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = newNode

    # Function for length of LinkList
    def len(self):
        length = 0
        lastNode = self.head
        while lastNode is not None:
            lastNode = lastNode.next
            length += 1
        return length

    # Searching element into LinkedList
    def search(self, newNode):
        if self.head is None:
            print("Nothing to Search..!! List is Empty.")
        else:
            lastNode = self.head
            while lastNode is not None:
                if newNode == lastNode.data:
                    print("The word is found in the list..!!")
                    return 1
                else:
                    lastNode = lastNode.next
            if lastNode is None:
                print("The word is not fount into the list..!!")
                return 0

    # Function to delete the element from last of the LinkedList
    def delete(self):
        if self.head is None:
            print("List is empty!! Nothing to delete.")
        else:
            lastNode = self.head
            llastNode = lastNode.next
            while llastNode is not None:
                lastNode = llastNode
                llastNode = llastNode.next
            lastNode.next = None
            llastNode.data = None

    # Delete a word from a position
    def delete_word(self, value):
        if self.head is None:
            print("List is empty!! Nothing to delete.")
        else:
            if self.head.data == value:
                self.head = self.head.next
            else:
                temp1 = self.head
                temp = self.head.next
                while temp is not None:
                    if temp.data == value:
                        temp1.next = temp.next
                        break
                    temp1 = temp1.next
                    temp = temp.next
                if temp is None:
                    print("Element not found.")

    # Traversing the element from LinkedList
    def traverse(self):
        if self.head is None:
            print("list is empty.")
            return
        currNode = self.head
        while True:
            if currNode is None:
                break
            print(currNode.data)
            currNode = currNode.next

    # Returning the data at given position
    def index(self, position):
        length = LinkedList.len(self)
        if 0 > position > length:
            print("Invalid input!!")
        else:
            currNode = self.head
            count = 1
            while count < position:
                currNode = currNode.next
                count += 1
            return currNode.data

    # Sorting the LinkedList
    def sortList(self, value):
        if self.head is None:
            self.head = value
        else:
            currNode = self.head
            if currNode.data > value.data:
                value.next = currNode
                self.head = value
            else:
                nextCurrNode = currNode.next
                while currNode.next is not None:
                    if nextCurrNode.data > value.data:
                        break
                    currNode = currNode.next
                    nextCurrNode = currNode.next
                value.next = nextCurrNode
                currNode.next = value
