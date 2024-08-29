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

def preorderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorderTraversal(rootNode.leftChild)
    preorderTraversal(rootNode.rightChild)
preorderTraversal(newBT)