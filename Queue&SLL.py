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





class SinglyLinkedList:
    def __init__(self):
        self.head = None 

    def isEmpty(self):
        return self.head is None  

    def append(self, data):
        new_node = {'data': data, 'next': None} 
        if self.isEmpty():
            self.head = new_node 
        else:
            current = self.head
            while current['next']: 
                current = current['next']
            current['next'] = new_node 

    def prepend(self, data):
        new_node = {'data': data, 'next': self.head}  
        self.head = new_node 

    def display(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(current['data'])  
            current = current['next']
        return nodes

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current['next']
        return count

    def delete(self, data):
        current = self.head
        if current is None:
            return  
        if current['data'] == data:  
            self.head = current['next']
            return

      
        while current['next']:
            if current['next']['data'] == data:
                current['next'] = current['next']['next']  
                return
            current = current['next']


linked_list = SinglyLinkedList()


linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.prepend(5)

print("Linked list contents:", linked_list.display())  # [5, 10, 20, 30]
print("Size of the list:", linked_list.size())  # 4

linked_list.delete(20)
print("Linked list after deleting 20:", linked_list.display())  # [5, 10, 30]

