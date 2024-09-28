from SLL import *

class Stack:
    def __init__(self):
        self.mylist=SLL()
        self.item_count=0
    
    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
        
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count-=1
            
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
    
    def size(self):
        if not self.is_empty():
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
