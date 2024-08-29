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
def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.heapList[index] < rootNode.heapList[parentIndex]:
            temp = rootNode.heapList[index]
            rootNode.heapList[index] = rootNode.heapList[parentIndex]
            rootNode.heapList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.heapList[index] > rootNode.heapList[parentIndex]:
            temp = rootNode.heapList[index]
            rootNode.heapList[index] = rootNode.heapList[parentIndex]
            rootNode.heapList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

def Insertion(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is Full"
    rootNode.heapList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"
    
newBinaryHeap=Heap(5)
Insertion(newBinaryHeap,4,'Max')
Insertion(newBinaryHeap,5,'Max')
Insertion(newBinaryHeap,2,'Max')
Insertion(newBinaryHeap,1,'Max')
LevelOrderTraversal(newBinaryHeap)