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

def searchBT(rootNode,target):
    if not rootNode:
        return
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootNode)
        while not (customqueue.isEmpty()):
            root=customqueue.dequeue()
            if root.value.data == target:
                return 'Aye'
            if (root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)
        return '404'

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

newBT=TreeNode('Drinks')
leftChild=TreeNode("Hot")
rightChild=TreeNode("Cold")
newBT.leftChild=leftChild
newBT.rightChild=rightChild          
newNode=TreeNode('Tea')
newNode1=TreeNode('Coffe')
newNode2=TreeNode('Cola')
inserNodeBT(newBT,newNode)
inserNodeBT(newBT,newNode1)
inserNodeBT(newBT,newNode2)
LevelOrderTraversal(newBT)