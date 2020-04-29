class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    # Function to add an element
    def push(self, value):
        if self.top is None:
            self.top = value
            self.count += 1
        else:
            value.next = self.top
            self.top = value
            self.count += 1

    # Function to remove an element
    def pop(self):
        if self.top is None:
            print("Stack is Empty.")
        else:
            if self.top.next is None:
                self.top = None
                self.count -= 1

    # Function for Peek an element
    def peek(self):
        if self.top is None:
            print("Stack is Empty.")
        else:
            return self.top.data

    # Checking the stack is empty or not
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    # size of the stack
    def size(self):
        return self.count
