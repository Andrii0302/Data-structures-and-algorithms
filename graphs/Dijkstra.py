import heapq
class Edge:
    def __init__(self,weight,start_vertex,target_vertex):
        self.weight=weight
        self.start_vertex=start_vertex
        self.target_vertex=target_vertex
class Node:
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.previous_node=None
        self.neighbors=[]
        self.min_distance=float('inf')

    def __lt__(self,other_node):
        return self.min_distance<other_node.min_distance
    
    def add_edge(self,weight, destination_vertex):
        self.neighbors.append(Edge(weight,self,destination_vertex))

class Dijkstra:
    def __init__(self):
        self.heap=[]

    def calculate(self,start_vertex):
        start_vertex.min_distance=0
        heapq.heappush(self.heap,start_vertex)
        while self.heap:
            actual_vertex=heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            for edge in actual_vertex.neighbors:
                start=edge.start_vertex
                target=edge.target_vertex
                new_distance=start.min_distance+edge.weight
                if new_distance < target.min_distance:
                    target.min_distance=new_distance
                    target.previous_node=start
                    heapq.heappush(self.heap,target)
            actual_vertex.visited=True
    def get_shortest_path(self,vertex):
        print(f"The shortest path is: {vertex.min_distance}")
        actual_vertex=vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=' ')
            actual_vertex=actual_vertex.previous_node

# CREAING NODES
nodeA=Node('A')
nodeB=Node('B')
nodeC=Node('C')
nodeD= Node('D')
nodeE= Node('E')
nodeF= Node('F')
nodeG= Node('G')
nodeH= Node('H')

# creating edges
nodeA.add_edge(6,nodeB)
nodeA.add_edge(10,nodeC)
nodeA.add_edge(9,nodeD)
nodeB.add_edge(5,nodeD)
nodeB.add_edge(16,nodeE)
nodeB.add_edge(13,nodeF)
nodeC.add_edge(6,nodeD)
nodeC.add_edge(5,nodeH)
nodeC.add_edge(21,nodeG)
nodeD.add_edge(8,nodeF)
nodeD.add_edge(7,nodeH)
nodeE.add_edge(10,nodeG)
nodeF.add_edge(4,nodeE)
nodeF.add_edge(12,nodeG)
nodeH.add_edge(14,nodeG)

ALGO=Dijkstra()
ALGO.calculate(nodeA)
ALGO.get_shortest_path(nodeG)