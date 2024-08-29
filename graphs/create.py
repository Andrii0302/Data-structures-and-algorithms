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

# custdict= {'a': ["b","c"],
#             "b" : ["a","d","e"],
#             "c":["a","e"],
#             "d": ["b",'e','f'],
#             'e': ['d','f','c'],
#             'f': ['d','e']}
g=Graph()
g.add_vertex('A')
g.add_vertex("E")
g.add_vertex('D')
g.addEdge('A','E')
g.addEdge('E','D')
g.remove_vertex('E')
g.print_graph()


