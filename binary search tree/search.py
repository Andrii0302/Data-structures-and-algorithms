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
def search(rootNode,Nvalue):
    if rootNode.data == Nvalue:
        print('Found')
    elif Nvalue < rootNode.data:
        if rootNode.leftChild.data== Nvalue:
            print("found")
        else:
            search(rootNode.leftChild,Nvalue)
    else:
        if rootNode.rightChild.data == Nvalue:
            print("found")
        else:
            search(rootNode.rightChild,Nvalue)
newBST=BST(None)
insertion(newBST, 60)
insertion(newBST,70)
insertion(newBST, 30)
insertion(newBST,40)
insertion(newBST, 160)
insertion(newBST,5)
levelOrder(newBST)
search(newBST, 40)




