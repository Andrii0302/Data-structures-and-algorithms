import linked_list_queue as queue
class AVLNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1

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
def get_height(rootNode):
    if not rootNode:
        return 0
    else:
        return rootNode.height
def right_rotation(disbalancednode):
    newRoot=disbalancednode.leftChild
    disbalancednode.leftChild=disbalancednode.leftCHild.rightChild
    newRoot.rightChild=disbalancednode
    disbalancednode.height=1+ max(get_height(disbalancednode.leftChild),get_height(disbalancednode.rightChild))
    newRoot.height=1+ max(get_height(newRoot.leftChild),get_height(newRoot.rightChild))
    return newRoot

def left_rotation(disbalancednode):
    newRoot=disbalancednode.rightChild
    disbalancednode.rightChild=disbalancednode.rightChild.leftChild
    newRoot.leftChild=disbalancednode
    disbalancednode.height=1+ max(get_height(disbalancednode.leftChild),get_height(disbalancednode.rightChild))
    newRoot.height=1+ max(get_height(newRoot.leftChild),get_height(newRoot.rightChild))
    return newRoot

def get_balance(rootNode):
    if not rootNode:
        return 0
    return get_height(rootNode.leftChild) - get_height(rootNode.rightChild)

def insertNode(rootNode,value):
    if not rootNode:
        return AVLNode(value)
    elif value < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, value)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, value)
    rootNode.height = 1 + max(get_height(rootNode.leftChild),get_height(rootNode.rightChild))
    balance = get_balance(rootNode)
    if balance > 1 and value < rootNode.leftChild.data:
        return right_rotation(rootNode)
    if balance > 1 and value > rootNode.leftChild.data:
        rootNode.leftChild=left_rotation(rootNode.leftChild)
        return right_rotation(rootNode)
    if balance < -1 and value > rootNode.rightChild.data:
        return left_rotation(rootNode)
    if balance < -1 and value < rootNode.rightChild.data:
        rootNode.rightChild=right_rotation(rootNode.rightChild)
        return left_rotation(rootNode)
    return rootNode
def clear(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    return 'The AVL is deleted'

AVL=AVLNode(5)
AVL=insertNode(AVL, 10)
AVL=insertNode(AVL, 15)
AVL=insertNode(AVL, 20)
clear(AVL)
levelOrder(AVL)