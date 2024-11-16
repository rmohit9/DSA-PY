class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next   

class Stack:
    def __init__(self):
        self.start=None
        self.item_count=0
        
    def is_empty(self):
        return self.start==None
    
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1
        
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise self.is_empty()
        
    def size(self):
        return self.item_count
    
#Driver Code
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

# O/P:    size of stack is 3
#         Top element is 60
#         removed element is 60

#         Top element is 90