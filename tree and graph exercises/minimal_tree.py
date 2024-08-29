class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def minimalTree(sortedArray):
    if not sortedArray:
        return None
    mid = len(sortedArray) // 2
    root = BSTNode(sortedArray[mid])
    
    root.left = minimalTree(sortedArray[:mid])
    
    root.right = minimalTree(sortedArray[mid+1:])
    
    return root

sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bst = minimalTree(sortedArray)

