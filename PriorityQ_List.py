class PriorityQueue:
    def __init__(self):
        self.item=[]
        
    def push(self,data,priority):
        index=0
        while index<len(self.item) and self.item[index][1]<=priority:
            index+=1
        self.item.insert(index,(data,priority))
        
    def is_empty(self):
        return len(self.item)==0
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.item.pop(0)[0]
    def size(self):
        return len(self.item)
    
#driver Code
p=PriorityQueue()
p.push("Amit",4)
p.push("Arjun",6)
p.push("Arihant",1)
p.push("Aman",4)
p.push("Ambika",2)

while not p.is_empty():
    print(p.pop())