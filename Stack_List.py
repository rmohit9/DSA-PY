class Stack:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    
    def push(self,data):
        self.items.append(data)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("stack is Empty")
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError
        
    def size(self):
        return len(self.items)
    
# Driver Code
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print('Removed Element is',s1.pop())
print("Top Element is",s1.peek())
            
            
# O/P:    Removed Element is 40
#         Top Element is 30