class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to represent the stack

    def isEmpty(self):
        return len(self.items) == 0  # Check if the stack is empty

    def push(self, item):
        self.items.append(item)  # Add an item to the top of the stack

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()  # Remove and return the top item from the stack

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]  # Return the top item without removing it

    def size(self):
        return len(self.items)  # Return the size of the stack

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())  # Output: 30
print("Stack size:", stack.size())  # Output: 3

print("Popped element:", stack.pop())  # Output: 30
print("Stack after pop:", stack.size())  # Output: 2






# Stack using a list

stack = []  # Initialize an empty list to represent the stack

# Pushing elements to the stack
stack.append(10)
stack.append(20)
stack.append(30)

print("Top element:", stack[-1])  # Output: 30 (peek the top element)
print("Stack size:", len(stack))  # Output: 3

# Popping elements from the stack
popped_item = stack.pop()
print("Popped element:", popped_item)  # Output: 30
print("Stack after pop:", len(stack))  # Output: 2
