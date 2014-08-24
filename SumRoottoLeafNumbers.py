__author__ = 'wxy325'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        self.sum = 0
        if root is None:
            return self.sum
        else:
            self.sumNode(root, "")
            return self.sum

    def sumNode(self, currentNode, currentStr):
        if currentNode is None:
            return
        elif currentNode.left is None and currentNode.right is None:
            newStr = currentStr + str(currentNode.val)
            if newStr != '':
                self.sum += int(newStr)
        else:
            newStr = currentStr + str(currentNode.val)
            self.sumNode(currentNode.left, newStr)
            self.sumNode(currentNode.right, newStr)
