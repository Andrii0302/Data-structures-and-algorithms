import linked_list_queue as queue
class AVLNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1

def preorderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorderTraversal(rootNode.leftChild)
    preorderTraversal(rootNode.rightChild)

def InorderTraversal(rootNode):
    if not rootNode:
        return
    
    InorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    InorderTraversal(rootNode.rightChild)
def PostOrderTraversal(rootNode):
    if not rootNode:
        return
    
    PostOrderTraversal(rootNode.leftChild)
    PostOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

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
AVL=AVLNode(10)