class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

newBT=TreeNode('Drinks')
leftChild=TreeNode("Hot")
rightChild=TreeNode("Cold")
newBT.leftChild=leftChild
newBT.rightChild=rightChild

def PostOrderTraversal(rootNode):
    if not rootNode:
        return
    
    PostOrderTraversal(rootNode.leftChild)
    PostOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
PostOrderTraversal(newBT)