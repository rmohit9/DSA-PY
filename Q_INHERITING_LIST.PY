class Queue(list):
    def __init__ (self):
        super().__init__()
    
    def is_empty(self):
        return len(self)==0
    
    def enqueue(self,data):
        self.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            return super().pop(0)
        else:
            raise IndexError('Queue is empty')
        
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError('Queue is empty')
        
    def get_rear(self):
        
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('Queue is empty')
        
    def size(self):
        return len(self)
    
        
#driver code
q1=Queue()
q1.enqueue(10)  
q1.enqueue(20)  
q1.enqueue(30)    
q1.enqueue(40)  
q1.enqueue(50) 
print("Queue has",q1.size(),"elements")

print("Front =",q1.get_front(),", Rear =",q1.get_rear())
try:
    print("removed element is ",q1.dequeue())
    print("Queue has now",q1.size(),"elements")
except IndexError as e:
    print(e.args[0])
