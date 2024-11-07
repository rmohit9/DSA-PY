class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
        
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        self.root=self.rinsert(self.root,data)              #here it is showing recursion method to recurse for the root
        
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left=self.rinsert(root.left,data)
        elif data > root.item:
            root.right=self.rinsert(root.right,data)
        return root    
        
    def search(self,data):
        return self.rsearch(self.root,data)
    
    def rsearch(self,root,data):
        if root is None or root.item==data:
            return root
        if data <root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
        
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root is not None:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
            
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root is not None:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
            
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root is not None:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)