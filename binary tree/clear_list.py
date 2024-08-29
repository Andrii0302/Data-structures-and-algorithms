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
    
    def level(self,index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
    def clear(self):
        self.customList=None
        return 'success'
newBinaryTree=BinaryTree(8)
newBinaryTree.insertNode('Drinks')
newBinaryTree.insertNode('Hot')
newBinaryTree.insertNode('Cold')
newBinaryTree.clear()
newBinaryTree.level(1)