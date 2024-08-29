class TreeNode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
def helper(node,minVal=float('-inf'),maxVal=float('inf')):
    if not node:
        return True
    val=node.val
    if val <= minVal or val >= maxVal:
        return False
    if not helper(node.right,val,maxVal):
        return False
    if not helper(node.left,minVal,val):
        return False
    return True

def isValidBST(root):
    return helper(root)
root1=TreeNode(2)
root1.left=TreeNode(1)
root1.right=TreeNode(4)
print(isValidBST(root1))
