class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def findNodeInTree(target,root):
    if not root:
        return False
    if root == target:
        return True
    else:
        return (findNodeInTree(target,root.left)) or findNodeInTree(target,root.right)

def findFirstCommonAncestor(n1, n2, root):
    n1onleft=findNodeInTree(n1,root.left)
    n2onleft=findNodeInTree(n2,root.left)
    if n1onleft ^ n2onleft:
        return root
    else:
        if n1onleft:
            return findFirstCommonAncestor(n1,n2,root.left)
        else:
            return findFirstCommonAncestor(n1,n2,root.right)

node54=Node(54)
node88=Node(88,node54)
