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
    disbalancednode.leftChild=disbalancednode.leftChild.rightChild
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
def minim(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return minim(rootNode.leftChild)

def pop_node(rootNode,value):
    if not rootNode:
        return rootNode
    elif value < rootNode.data:
        rootNode.leftChild = pop_node(rootNode.leftChild,value)
    elif value > rootNode.data:
        rootNode.rightChild = pop_node(rootNode.rightChild,value)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode=None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode=None
            return temp
        temp = minim(rootNode.rightChild)
        rootNode.data=temp.data
        rootNode.rightChild=pop_node(rootNode.rightChild, temp.data)
    rootNode.height = 1 + max(get_height(rootNode.leftChild),get_height(rootNode.rightChild))
    balance=get_balance(rootNode)
    if balance > 1 and get_balance(rootNode.leftChild)>=0:
        return right_rotation(rootNode)
    if balance > 1 and get_balance(rootNode.leftChild) <0:
        rootNode.leftChild=left_rotation(rootNode.leftChild)
        return right_rotation(rootNode)
    if balance < -1 and get_balance(rootNode.rightChild) <=0:
        return left_rotation(rootNode)
    if balance < -1 and get_balance(rootNode.rightChild) >0:
        rootNode.rightChild=right_rotation(rootNode.rightChild)
        return left_rotation(rootNode)
    return rootNode

    
    
AVL=AVLNode(5000)
AVL=insertNode(AVL, 10)
# AVL=insertNode(AVL, 15)
# AVL=insertNode(AVL, 20)
# AVL=pop_node(AVL, 15)
levelOrder(AVL)