import linked_list_queue as queue
from random import randint
class BST:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertion(rootNode, value):
    if rootNode.data == None:
        rootNode.data = value
    elif value <= rootNode.data:
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

def minim(rootNode):
    current = rootNode
    while current.leftChild is not None:
        current = current.leftChild
    return current

def delete(rootNode, value):
    traversed_nodes = 0
    single_rotations = 0
    
    if rootNode is None:
        return rootNode, traversed_nodes, single_rotations
    
    traversed_nodes += 1
    
    if value < rootNode.data:
        rootNode.leftChild, nodes, rotations = delete(rootNode.leftChild, value)
        traversed_nodes += nodes
        single_rotations += rotations
    elif value > rootNode.data:
        rootNode.rightChild, nodes, rotations = delete(rootNode.rightChild, value)
        traversed_nodes += nodes
        single_rotations += rotations
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp, traversed_nodes, single_rotations
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp, traversed_nodes, single_rotations
        temp = minim(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild, nodes, rotations = delete(rootNode.rightChild, temp.data)
        traversed_nodes += nodes
        single_rotations += rotations

    return rootNode, traversed_nodes, single_rotations

def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customqueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customqueue.enqueue(root.value.rightChild)

traversed_nodes_total = 0
single_rotations_total = 0
operations = 200000
num_iterations = 10

for i in range(num_iterations):
    newBST = BST(None)
    for i in range(1000000):
        insertion(newBST, randint(1, 10000))

    for i in range(operations):
        value_to_delete = randint(1, 10000)
        newBST, traversed_nodes, single_rotations = delete(newBST, value_to_delete)
        traversed_nodes_total += traversed_nodes
        single_rotations_total += single_rotations

print("Average traversed nodes per deletion:", traversed_nodes_total / (num_iterations * operations))
print("Average single rotations per deletion:", single_rotations_total / (num_iterations * operations))

