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

def heapifyExtract(rootNode, index, heapType):
    leftIndex=index*2
    rightIndex=index*2+1
    swapChild=0
    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType=='Min':
            if rootNode.heapList[index]>rootNode.heapList[leftIndex]:
                temp=rootNode.heapList[index]
                rootNode.heapList[index]=rootNode.heapList[leftIndex]
                rootNode.heapList[leftIndex]=temp
            return
        elif heapType=='Max':
            if rootNode.heapList[index]<rootNode.heapList[leftIndex]:
                temp=rootNode.heapList[index]
                rootNode.heapList[index]=rootNode.heapList[leftIndex]
                rootNode.heapList[leftIndex]=temp
            return
    else:
        if heapType=='Min':
            if rootNode.heapList[leftIndex]<rootNode.heapList[rightIndex]:
                swapChild=leftIndex
            else:
                swapChild=rightIndex
            if rootNode.heapList[index]>rootNode.heapList[swapChild]:
                    temp=rootNode.heapList[index]
                    rootNode.heapList[index]=rootNode.heapList[swapChild]
                    rootNode.heapList[swapChild]=temp
        else:
            if rootNode.heapList[leftIndex]>rootNode.heapList[rightIndex]:
                swapChild=leftIndex
            else:
                swapChild=rightIndex
            if rootNode.heapList[index]<rootNode.heapList[swapChild]:
                    temp=rootNode.heapList[index]
                    rootNode.heapList[index]=rootNode.heapList[swapChild]
                    rootNode.heapList[swapChild]=temp
        heapifyExtract(rootNode, swapChild, heapType)
def Extract(rootNode,heapType):
    if rootNode.heapSize==0:
        return
    else:
        extracted=rootNode.heapList[1]
        rootNode.heapList[1]=rootNode.heapList[rootNode.heapSize]
        rootNode.heapList[rootNode.heapSize]=None
        rootNode.heapSize-=1
        heapifyExtract(rootNode, 1, heapType)
        return extracted
    
newBinaryHeap=Heap(5)
Insertion(newBinaryHeap,4,'Max')
Insertion(newBinaryHeap,5,'Max')
Insertion(newBinaryHeap,2,'Max')
Insertion(newBinaryHeap,1,'Max')
Extract(newBinaryHeap,'Max')

LevelOrderTraversal(newBinaryHeap)