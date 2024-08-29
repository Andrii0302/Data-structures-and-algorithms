import linked_list_queue as queue
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

def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root=customqueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customqueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customqueue.enqueue(root.value.rightChild)
def clear(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    return 'deleted'
newBST=BST(None)
insertion(newBST, 60)
insertion(newBST,70)
insertion(newBST, 30)
insertion(newBST,40)
insertion(newBST, 160)
insertion(newBST,5)
clear(newBST)
levelOrder(newBST)

