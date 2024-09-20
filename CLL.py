class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
class CLL:
    def __init__(self,last=None):
        self.last=last
        
    def is_empty(self):
        return self.last==None
    
    def insert_at_start(self,data):
        n=(data,self.last.next)
        while self.last != None:
            n.next=self.last.next
        self.last=n
        
    def print_list(self):
        temp=self.last.next
        while temp != self.last.next:
            print(temp,end=' ')
            temp=temp.next
        
#driver code
mylist =CLL()
mylist.insert_at_start(10)
mylist.print_list()
print()
    