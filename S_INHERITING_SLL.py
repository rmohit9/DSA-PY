from SLL import *
class Stack(SLL):
    
    def __init__(self):
        self.item_count=0
        super().__init__()
    
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1
        
        
    def pop(self):
        if not self.is_empty():
            data=self.start.item  #fro capturing the value to be popped
            self.delete_first()
            self.item_count-=1
            return data
            
        else:
            raise IndexError("Stack Overflow")
            
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack Underflow")
        
    def size(self):
        return self.item_count
    
#driver code
s1=Stack()
s1.push(20)
s1.push(30)
s1.push(60)
print("size of stack is",s1.size())
print("Top element is",s1.peek())
print("removed element is",s1.pop())
print()
s1.push(40)
s1.push(90)
print("Top element is",s1.peek())
            
        
    
        
        
        
    