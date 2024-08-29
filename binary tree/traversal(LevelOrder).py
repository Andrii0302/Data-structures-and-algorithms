import linked_list_queue as queue
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

def LevelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootNode)
        while not (customqueue.isEmpty()):
            root=customqueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)
LevelOrderTraversal(newBT)
