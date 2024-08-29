class BinaryTree:
    def __init__(self,size):
        self.customList=size * [None]
        self.lastUsedIndex=0
        self.maxSize=size
    
newBinaryTree=BinaryTree(8)