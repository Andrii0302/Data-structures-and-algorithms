class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        queue=[]
        queue.append([startNode])
        while queue:
            path=queue.pop(0)
            node=path[-1]
            if node == endNode:
                return True
            for i in self.gdict.get(node,[]):
                new=list(path)
                new.append(i)
                queue.append(new)
        return False
            