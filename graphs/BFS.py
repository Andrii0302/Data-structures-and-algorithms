from collections import deque
class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    def add_vertex(self,vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex]=[]
            return True
        return False
    def print_graph(self):
        for vertex in self.gdict:
            print(vertex,":",self.gdict[vertex])
    def addEdge(self,vertex,edge):
        if vertex in self.gdict.keys() and edge in self.gdict.keys():
            self.gdict[vertex].append(edge)
            self.gdict[edge].append(vertex)
            return True
        return False
    def removeEdge(self,vertex,edge):
        if vertex in self.gdict.keys() and edge in self.gdict.keys():
            try:
                self.gdict[vertex].remove(edge)
                self.gdict[edge].remove(vertex)
            except ValueError:
                pass
            return True
        return False
    def remove_vertex(self,vertex):
        if vertex in self.gdict.keys():
            for other_vertex in self.gdict[vertex]:
                self.gdict[other_vertex].remove(vertex)
            del self.gdict[vertex]
            return True
        return False

    def bfs(self,vertex):
        visited=set()
        visited.add(vertex)
        queue=deque([vertex])
        while queue:
            current_vertex=queue.popleft()
            print(current_vertex)
            for adjacent_vertex in self.gdict[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)

g=Graph()
for i in ['A','B','C','D','E']:
    g.add_vertex(i)
g.addEdge('A','B')
g.addEdge('A','C')
g.addEdge('C','D')
g.addEdge('E','D')
g.addEdge('E','B')
g.bfs('A')
