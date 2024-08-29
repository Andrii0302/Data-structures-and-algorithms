class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def get_height(root):
    if not root:
        return 0
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return max(left_height, right_height) + 1

def isBalanced(root):
    if not root:
        return True

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)

print(isBalanced(root))