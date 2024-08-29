import linked_list_queue as queue
import random
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

def delete_node(rootNode, value):
    if not rootNode:
        return rootNode, 0, 0
    nodes_visited = 0
    rotations_done = 0
    
    if value < rootNode.data:
        rootNode.leftChild, left_nodes_visited, left_rotations_done = delete_node(rootNode.leftChild, value)
        nodes_visited += left_nodes_visited + 1
        rotations_done += left_rotations_done
    elif value > rootNode.data:
        rootNode.rightChild, right_nodes_visited, right_rotations_done = delete_node(rootNode.rightChild, value)
        nodes_visited += right_nodes_visited + 1
        rotations_done += right_rotations_done
    else:
        
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp, nodes_visited + 1, rotations_done
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp, nodes_visited + 1, rotations_done
        
        temp = minim(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild, right_nodes_visited, right_rotations_done = delete_node(rootNode.rightChild, temp.data)
        nodes_visited += right_nodes_visited
        rotations_done += right_rotations_done


    rootNode.height = 1 + max(get_height(rootNode.leftChild), get_height(rootNode.rightChild))

    balance = get_balance(rootNode)

    
    if balance > 1 and get_balance(rootNode.leftChild) >= 0:
        return right_rotation(rootNode), nodes_visited, rotations_done + 1
    if balance > 1 and get_balance(rootNode.leftChild) < 0:
        rootNode.leftChild = left_rotation(rootNode.leftChild)
        return right_rotation(rootNode), nodes_visited, rotations_done + 2
    if balance < -1 and get_balance(rootNode.rightChild) <= 0:
        return left_rotation(rootNode), nodes_visited, rotations_done + 1
    if balance < -1 and get_balance(rootNode.rightChild) > 0:
        rootNode.rightChild = right_rotation(rootNode.rightChild)
        return left_rotation(rootNode), nodes_visited, rotations_done + 2

    return rootNode, nodes_visited, rotations_done
def generate_random_values(n):
    return random.sample(range(1, 1000001), n)
def perform_experiment(iterations):
    results = []
    for _ in range(iterations):
        
        avl_tree = AVLNode(500000)  
        random_values = generate_random_values(1000000)
        for value in random_values:
            avl_tree = insertNode(avl_tree, value)


        initial_height = get_height(avl_tree)

        
        deletion_values = random.sample(random_values, 1000000)
        total_traversed_nodes = 0
        total_rotations = 0
        for value in deletion_values:
            traversed_nodes = 0
            rotations = 0
    
            avl_tree, nodes_visited, rotations_done = delete_node(avl_tree, value)
            total_traversed_nodes += nodes_visited
            total_rotations += rotations_done
        results.append((total_traversed_nodes, total_rotations))

    
    mean_traversed_nodes = sum(result[0] for result in results) / iterations
    mean_rotations = sum(result[1] for result in results) / iterations

    return mean_traversed_nodes, mean_rotations, initial_height

print(perform_experiment(10))
