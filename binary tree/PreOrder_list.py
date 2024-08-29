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
    
    def PreOrder(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.PreOrder(index*2)
        self.PreOrder(index*2+1)

newBinaryTree=BinaryTree(8)
newBinaryTree.insertNode('Drinks')
newBinaryTree.insertNode('Hot')
newBinaryTree.insertNode('Cold')
newBinaryTree.PreOrder(1)


