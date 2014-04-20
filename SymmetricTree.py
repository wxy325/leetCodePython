# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean

    def visit(self, lNode, rNode):

        if lNode is None and rNode is None:
            return True
        elif lNode is None or rNode is None:
            return False
        
        if lNode.val != rNode.val:
            return False
        if not self.visit(lNode.left, rNode.right) or not self.visit(lNode.right, rNode.left):
            return False
        return True

    def isSymmetric(self, root):
        if root is None:
            return True
        return self.visit(root.left, root.right)
