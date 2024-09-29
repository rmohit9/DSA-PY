class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,data):
        self.append(data)
        
    def pop(self):
        if not self.is_empty():
            return super().pop()           #to avoud override and use parent class pop() not the overrided one
        else:
            raise IndexError("stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self[-1]               #here stack object==list object
        else:
            raise IndexError("stack is empty")
        
    def size(self):
        return len(self)
    
    def insert(self,index,data):
        raise AttributeError("No such attrubute 'insert' in stack")

    # Driver Code 
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top Element=", s1.peek())
print("Removed Element",s1.pop())
print("Top Element=", s1.peek())
print("Removed Element",s1.pop())
print("Top Element=", s1.peek())
print()
        
        
    
            