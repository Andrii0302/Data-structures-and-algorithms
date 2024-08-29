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
    
    def level(self,index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
    def delete(self,value):
        if self.lastUsedIndex == 0:
            return 'empty'
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i]=self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex]=None
                self.lastUsedIndex-=1
                return 'deleted'
newBinaryTree=BinaryTree(8)
newBinaryTree.insertNode('Drinks')
newBinaryTree.insertNode('Hot')
newBinaryTree.insertNode('Cold')
newBinaryTree.delete('Drinks')
newBinaryTree.level(1)