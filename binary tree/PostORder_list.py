class BinaryTree:
    def __init__(self,size):
        self.customList=size * [None]
        self.lastUsedIndex=0
        self.maxSize=size
    
    def insertNode(self,value):
        if self.lastUsedIndex+1 == self.maxSize:
            return 'Tree is full'
        self.customList[self.lastUsedIndex+1]=value
        self.lastUsedIndex+=1
        return 'Inserted'
    def searchNode(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i]==nodeValue:
                return 'success'
        return "not found"
    
    def PostOrder(self,index):
        if index > self.lastUsedIndex:
            return
        self.PostOrder(index*2)
        self.PostOrder(index*2+1)
        print(self.customList[index])

newBinaryTree=BinaryTree(8)
newBinaryTree.insertNode('Drinks')
newBinaryTree.insertNode('Hot')
newBinaryTree.insertNode('Cold')
newBinaryTree.PostOrder(1)