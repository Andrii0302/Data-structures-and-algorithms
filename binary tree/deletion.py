import linked_list_queue as queue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

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

def inserNodeBT(rootNode,newNode):
    if not rootNode:
        rootNode=newNode
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootNode)
        while not (customqueue.isEmpty()):
            root=customqueue.dequeue()
            if root.value.leftChild is not None:
                customqueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild=newNode
                return 'inserted'
            if root.value.rightChild is not None:
                customqueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild=newNode
                return 'inserted'

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root=customqueue.dequeue()
            if (root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)
        deepestNode=root.value
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root=customqueue.dequeue()
            if root.value is dNode:
                root.value=None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild=None
                    return
                else:
                    customqueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild=None
                    return
                else:
                    customqueue.enqueue(root.value.leftChild)

def deleteNodeBT(rootNode,node):
    if not rootNode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root=customqueue.dequeue()
            if root.value.data==node:
                dNode=getDeepestNode(rootNode)
                root.value.data=dNode.data
                deleteDeepestNode(rootNode,dNode)
                return 'deleted'
            if (root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)
        return 'Failed'

newBT=TreeNode('Drinks')
leftChild=TreeNode("Hot")
rightChild=TreeNode("Cold")
newBT.leftChild=leftChild
newBT.rightChild=rightChild          
newNode=TreeNode('Tea')
newNode1=TreeNode('Coffee')
newNode2=TreeNode('Cola')
inserNodeBT(newBT,newNode)
inserNodeBT(newBT,newNode1)
inserNodeBT(newBT,newNode2)
deepestNode= getDeepestNode(newBT)
deleteDeepestNode(newBT,deepestNode)
deleteNodeBT(newBT,'Coffee')
LevelOrderTraversal(newBT)
