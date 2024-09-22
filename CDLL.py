class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
        
class CDLL:
    def __init__(self,start):
        self.start=start
        
    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        n= Node(data)
        if self.is_empty():
            self.start=n
        elif self.start.next== self.start:
            n.next=self.start
            n.prev=self.start
            self.start.prev=n
            self.start=n
        else:
            n.next==self.start.next
            n.prev=self.start
            self.start.next.prev=n
            self.start.next=n
                
        
            
            