class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)  # Adds items at the end of the list

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)  # Removes items from the front of the list

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

q = Queue()
q.enqueue(12)
q.enqueue(34)
q.enqueue(56)

q.dequeue()  # Removes 12 from the front of the queue

print(q.size())  # Prints the size of the queue
print("Queue contents:", q.display())  # Prints the current contents of the queue






# Define the Node class to represent each node in the list
class Node:
    def __init__(self, data):
        self.data = data  # Holds the data for the node
        self.next = None  # Points to the next node in the list (initially None)

# Define the SinglyLinkedList class
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty, so head is None

    def isEmpty(self):
        return self.head is None  # Check if the list is empty

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.isEmpty():
            self.head = new_node  # If the list is empty, the new node becomes the head
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Add the new node at the end of the list

    def prepend(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # New node points to the current head
        self.head = new_node  # The new node becomes the head of the list

    def display(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(current.data)  # Add each node's data to the list
            current = current.next  # Move to the next node
        return nodes

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def delete(self, data):
        current = self.head
        if current is None:
            return  # List is empty, nothing to delete

        if current.data == data:  # If the head node has the data to delete
            self.head = current.next
            return

        # Traverse the list to find the node to delete
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # Bypass the node to delete it
                return
            current = current.next

# Example usage:
linked_list = SinglyLinkedList()

# Append data to the linked list
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

# Prepend data to the linked list
linked_list.prepend(5)

# Display the list and size
print("Linked list contents:", linked_list.display())  # [5, 10, 20, 30]
print("Size of the list:", linked_list.size())  # 4

# Delete a node with value 20
linked_list.delete(20)
print("Linked list after deleting 20:", linked_list.display())  # [5, 10, 30]





#this is using dictionary
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty, so head is None

    def isEmpty(self):
        return self.head is None  # Check if the list is empty

    def append(self, data):
        new_node = {'data': data, 'next': None}  # Create a new node as a dictionary
        if self.isEmpty():
            self.head = new_node  # If the list is empty, the new node becomes the head
        else:
            current = self.head
            while current['next']:  # Traverse to the last node
                current = current['next']
            current['next'] = new_node  # Add the new node at the end of the list

    def prepend(self, data):
        new_node = {'data': data, 'next': self.head}  # New node points to the current head
        self.head = new_node  # The new node becomes the head of the list

    def display(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(current['data'])  # Add each node's data to the list
            current = current['next']  # Move to the next node
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
            return  # List is empty, nothing to delete

        if current['data'] == data:  # If the head node has the data to delete
            self.head = current['next']
            return

        # Traverse the list to find the node to delete
        while current['next']:
            if current['next']['data'] == data:
                current['next'] = current['next']['next']  # Bypass the node to delete it
                return
            current = current['next']

# Example usage:
linked_list = SinglyLinkedList()

# Append data to the linked list
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

# Prepend data to the linked list
linked_list.prepend(5)

# Display the list and size
print("Linked list contents:", linked_list.display())  # [5, 10, 20, 30]
print("Size of the list:", linked_list.size())  # 4

# Delete a node with value 20
linked_list.delete(20)
print("Linked list after deleting 20:", linked_list.display())  # [5, 10, 30]

