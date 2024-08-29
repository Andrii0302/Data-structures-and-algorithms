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

def InorderTraversal(rootNode):
    if not rootNode:
        return
    
    InorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    InorderTraversal(rootNode.rightChild)
InorderTraversal(newBT)