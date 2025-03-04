#queue using class:
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

q = Queue()
q.enqueue(12)
q.enqueue(34)
q.enqueue(56)
q.dequeue()
q.enqueue(90)
print(q.size())

print("Queue contents:", q.display()) 
