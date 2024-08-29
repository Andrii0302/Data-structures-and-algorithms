class AVLNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1

def search(rootNode,Nvalue):
    if rootNode.data == Nvalue:
        print('Found')
    elif Nvalue < rootNode.data:
        if rootNode.leftChild.data== Nvalue:
            print("found")
        else:
            search(rootNode.leftChild,Nvalue)
    else:
        if rootNode.rightChild.data == Nvalue:
            print("found")
        else:
            search(rootNode.rightChild,Nvalue)

AVL=AVLNode(10)