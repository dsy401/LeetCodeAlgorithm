# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        return self.helper(root,val)



    def helper(self,root,val):
        if root != None:
            if val >= root.val:
                if root.right == None:
                    root.right = TreeNode(val)
                else:
                    self.helper(root.right, val)
            else:
                if root.left == None:
                    root.left = TreeNode(val)
                else:
                    self.helper(root.left, val)
        return root

a = Solution()

node = TreeNode(4)
node.left = TreeNode(2)
node.right = TreeNode(7)
node.left.left = TreeNode(1)
node.left.right = TreeNode(3)

