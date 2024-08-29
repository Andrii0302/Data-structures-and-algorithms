class Heap:
    def __init__(self,size):
        self.heapList = (size+1) *[None]
        self.heapSize = 0
        self.maxSize=size+1

def peek(rootNode):
        if not rootNode:
            return None
        return rootNode.heapList[1] 
def sizeOf(rootNode):
    if not rootNode:
            return 0
    return rootNode.heapSize
# def InOrederTraversal(rootNode):
#     if not rootNode:
#         return
#     else:
#         print(rootNode.heapList[1])
#         InOrederTraversal(rootNode.heapList[2])
#         InOrederTraversal(rootNode.heapList[3])
def LevelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.heapList[i])
newBinaryHeap=Heap(5)
print(LevelOrderTraversal(newBinaryHeap))