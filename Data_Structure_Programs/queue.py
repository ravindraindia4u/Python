class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self, value):
        if self.rear is None:
            self.front = self.rear = value
            self.count += 1
        else:
            self.rear.next = value
            self.rear = value
            self.count += 1

    def dequeue(self):
        if Queue.isEmpty(self):
            print("Queue is empty, Nothing to dequeue!!")
        else:
            if self.front is None:
                self.front = None
            else:
                self.front = self.front.next
                self.count -= 1

    def isEmpty(self):
        if self.rear is None:
            return True
        else:
            return False

    def size(self):
        if self.count <= 0:
            print("queue is empty!!")
        return self.count

    def traverse(self):
        if self.count == 0:
            print("Queue is empty!!")
        else:
            curNode = self.front
            while curNode is not None:
                print(curNode.data)
                curNode = curNode.next
