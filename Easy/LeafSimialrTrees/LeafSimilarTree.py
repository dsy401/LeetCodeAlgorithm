# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def find_leaf(self,root,result):
        if root is None:
            return result
        if root.left is None and root.right is None:
            result.append(root.val)
            return result
        self.find_leaf(root.left,result)
        self.find_leaf(root.right,result)
        return result

    def leafSimilar(self, root1, root2):
        return self.find_leaf(root1,[]) == self.find_leaf(root2,[])