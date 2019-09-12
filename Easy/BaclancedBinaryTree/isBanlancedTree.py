# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def treeDepth(self,root):
        if root == None:
            return 0
        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)
        if left > right:
            left+=1
            return left
        else:
            right+=1
            return right

    def isBalanced(self, root):
        if root == None:
            return True
        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)
        diff = abs(left-right)
        if diff>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)