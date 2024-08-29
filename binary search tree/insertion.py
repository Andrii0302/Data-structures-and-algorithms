class BST:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

def insertion(rootNode,value):
    if rootNode.data==None:
        rootNode.data=value
    elif value <=rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BST(value)
        else:
            insertion(rootNode.leftChild, value)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BST(value)
        else:
            insertion(rootNode.rightChild, value)
    return 'Success'


newBST=BST(None)
insertion(newBST, 60)
insertion(newBST,70)
print(newBST.data)
print(newBST.rightChild.data)