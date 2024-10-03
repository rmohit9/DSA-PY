from SLL import *
class Queue(SLL):
    
    def __init__ (self):
        super().__init__()
        self.item_count=0
        
    def is_empty(self):
        return super().is_empty()
    
    def enqueue(self,data):
        self.insert_at_last(data)
        self.item_count+=1
        
    def dequeue(self):
        data=self.start.item
        self.delete_first()
        self.item_count-=1
        return data
        
    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("EMPTY STACK")
        
    def size(self):
        return self.item_count
    
#Driver code
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)        
q1.enqueue(40)

print("Front Item =",q1.get_front())
print("Size is =",q1.size())
q1.dequeue()
print("Front Item =",q1.get_front())
print("Size is =",q1.size())
    
        
        
        