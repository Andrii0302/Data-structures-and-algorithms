class Heap:
    def __init__(self,size):
        self.heapList = (size+1) *[None]
        self.heapSize = 0
        self.maxSize=size+1

def peek(rootNode):
        if not rootNode:
            return None
        return rootNode.heapList[1] 
newBinaryHeap=Heap(5)