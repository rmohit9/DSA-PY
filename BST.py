class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
        
class BST:
    def __init__(self):
        self.root=None
    
    #defining the insert method to store new data item in the binary search tree    
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
    
    #defining a search method to find item in BST and returns the node reference      
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.item==data:
            return root
        if data <root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
    
    #inorder traversing    
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root is not None:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
            
    #preorder traversing
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root is not None:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    
    #postorder traversing        
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root is not None:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
    
    #retrieving the maximum and minimun values/nodes of BST        
    def min_value(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.item 
    
    def max_value(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item 
    
    #defining the method to delete a node from BST
    def delete(self,data):
        self.root=self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return root
        if data < root.item:
            root.left=self.rdelete(root.left,data)
        elif data > root.item:
            root.right=self.rdelete(root.right,data)
        else:  #(it runs when self.data==root.item)
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
           #(it runs when the deleting node contains two childs)
            root.item=self.min_value(root.right)
            self.rdelete(root.right,root.item)
        return root    
                 
    #defining a size method to return the number of elements present in the BST
    def size(self):
        return len(self.inorder())         