class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list={ v :[] for v in range(vno)} 
        
    def add_edge(self,v,u,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            #here it is describing the adjacency vertex with weight
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print("Invalid verices")
            
    def remove_edge(self,v,u):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            #here it is describing the adjacency vertex with weight
            self.adj_list[u]=[(vertex,weight)for vertex,weight in self.adj_list[u] if vertex!=v]
            self.adj_list[v]=[(vertex,weight)for vertex,weight in self.adj_list[v] if vertex!=u]
        else:
            print("Invalid vertices") 
            
    def has_range(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex == v for vertex,x in self.adj_list[u])
        else:
            print("invalid vertex")
            
    def print_adj_list(self):
        for vertex,n in self.adj_list.items():
            print("v",vertex,":",n)
 
#driver code           
g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.print_adj_list()

# O/P:
#   	v 0 : [(1, 1)]
#       v 1 : [(0, 1), (2, 1), (3, 1)]
#       v 2 : [(1, 1), (4, 1)]
#       v 3 : [(1, 1), (4, 1)]
#       v 4 : [(2, 1), (3, 1)]



            
        