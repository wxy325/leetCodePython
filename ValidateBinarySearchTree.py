# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidBST(root):
    if not root:
        return True

    node = root
    if node.left:
        if node.left.val < node.val:
            tempRight = node.left
            while tempRight.right:
                tempRight = tempRight.right
            if tempRight.val < node.val:
                if not isValidBST(node.left):
                    return False
            else:
                return False
        else:
            return False

    if node.right:
        if node.right.val > node.val:
            tempLeft = node.right
            while tempLeft.left:
                tempLeft = tempLeft.left
            if tempLeft.val > node.val:
                if not isValidBST(node.right):
                    return False
            else:
                return False
        else:
            return False

    return True