class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next
        
class PriorityQueue:
    def __init__(self):
        self.start=None
        self.item_count=0
        
    def push(self,data,priority):
        n=Node(data,priority)
        if self.start==None or priority <self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next != None and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1
            
    def is_empty(self):
        return self.start==None
            
    def pop(self):
        if self.is_empty():
            raise IndexError("PriorrityQ is empty")
        data=self.start.item
        self.start=self.start.next
        self.item_count-=1
        return data
    
#driver Code
p=PriorityQueue()
p.push("Amit",4)
p.push("Arjun",6)
p.push("Arihant",1)
p.push("Aman",4)
p.push("Ambika",2)

while not p.is_empty():
    print(p.pop())
    
# O/P: 
# Arihant
# Ambika
# Amit
# Aman
# Arjun
    
                
                
               
    