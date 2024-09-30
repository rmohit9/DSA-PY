class Queue:
    def __init__(self):
        self.item=[]
        
    def is_empty(self):
        return len(self.item)==0
    
    def enqueue(self,data):
        self.item.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)
        else:
            raise IndexError("Queue is empty")
        
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError("Queue is Empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Queue is empty")
        
    def size(self):
        return len(self.item)
    
#Driver Code 
q1=Queue()

try:                           #if queue is empty
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
    
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



# print("Size of queue is ",q1.size())  
        
        
        