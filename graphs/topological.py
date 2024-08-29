from collections import defaultdict

class Graph:
    def __init__(self,numver):
        self.graph = defaultdict(list)
        self.numver=numver
    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)
    
    def topological_sort_util(self,v,visited,stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topological_sort_util(i,visited,stack)
        stack.insert(0,v)
    
    def topological_sort(self):
        visited=[]
        stack=[]
        for i in list(self.graph):
            if i not in visited:
                self.topological_sort_util(i,visited,stack)
        print(stack)
    def print_graph(self):
        for i in self.graph:
            print(i,":",self.graph[i])
g=Graph(8)
g.addEdge('A','C')
g.addEdge('C','E')
g.addEdge('E','H')
g.addEdge('E','F')
g.addEdge('F','G')
g.addEdge('B','D')
g.addEdge('B','C')
g.addEdge('D','F')

g.topological_sort()
