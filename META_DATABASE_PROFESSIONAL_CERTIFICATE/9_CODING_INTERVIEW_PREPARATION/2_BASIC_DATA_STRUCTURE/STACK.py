#python

class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append()

    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cant pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek From empty stacks")
        
    def size(self):
        return len(self.items)
    

