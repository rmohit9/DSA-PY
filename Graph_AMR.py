class Graph:
    #defining the adjacency matrix with vertex count
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_matrix=[ [0]*vno for e in range(vno)]
        
    #defining a method to add an edge in the graph with given weight
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("Invalid vertex") 
            
    #defining a method to remove an edge from the graph with given weight
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("Invalid vertex")
    
    #defining the method to check whether the node contains edge or not
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("Invalid vertex")

    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
           print(" ".join(map(str,row_list)))
            
g= Graph(5)
g.add_edge(0,1) 
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4) 

g.print_adj_matrix() 

#O/P:   0 1 0 0 0
#       1 0 1 1 0
#       0 1 0 1 0
#       0 1 1 0 1
#       0 0 0 1 0
                