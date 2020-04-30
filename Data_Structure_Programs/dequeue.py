class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Dequeue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0

    def addFront(self, value):
        if self.rear is None:
            self.rear = self.front = value
            self.count += 1
        else:
            value.next = self.front
            self.front = value
            self.count += 1

    def addRear(self, value):
        if self.rear is None:
            self.rear = self.front = value
            self.count += 1
        else:
            self.rear.next = value
            self.rear = value
            self.count += 1

    def removeFront(self):
        if self.rear is None:
            print("Queue is empty!! Nothing to remove.")
        else:
            if self.front == self.rear:
                node_data = self.front.data
                self.front = self.rear = None
                self.count -= 1
                return  node_data
            else:
                node_data = self.front.data
                self.front = self.front.next
                self.count -= 1
                return node_data

    def removeRear(self):
        if self.rear is None:
            print("Queue is empty!! nothing to remove.")
        else:
            if self.front == self.rear:
                node_data = self.front.data
                self.front = self.rear = None
                self.count -= 1
                return node_data
            else:
                node_data = self.rear.data
                temp = self.front
                while temp.next != self.rear:
                    temp = temp.next
                self.rear = temp
                temp.next = None
                self.count -= 1
                return node_data

    def isEmpty(self):
        if self.rear is None:
            return True
        else:
            return False

    def size(self):
        return self.count

    def traverse(self):
        if self.rear is None:
            print("Queue is empty!!")
        else:
            currNode = self.front
            while currNode is not None:
                print(currNode.data)
                currNode = currNode.next
