class Stack:
    def __init__(self):
        self.stack=[]
    
    def is_empty(self):
        return len(self.stack) == 0

    def push(self,element):
        return self.stack.append(element)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("stack is empty")
            
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else :
            print("stack is empty")
            
    def display(self):
        if not self.is_empty():
            print("Current Stack:", self.stack)
        else:
            print("Stack is empty!")
            
s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display() 
print("Popped item:", s.pop())  # Output: 30
s.display() 
print("peek element " , s.peek())


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
