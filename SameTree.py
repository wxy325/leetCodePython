__author__ = 'wxy325'

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree noddde
    # @return a boolean
    def isSameTree(self, p, q):
        return self.visitTree(p,q)


    def visitTree(self, a, b):
        if a == None:
            if b == None:
                return True
            else:
                return False
        elif b == None:
            return False

        if a.val != b.val:
            return False
        if not self.visitTree(a.left, b.left):
            return False
        if not self.visitTree(a.right, b.right):
            return False
        return True

