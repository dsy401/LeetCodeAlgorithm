# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        result = []
        stack = []

        def helper(root,acc):
            if root == None:
                return
            acc += root.val
            stack.append(root.val)
            if root.left == None and root.right == None:
                if acc == sum:
                    result.append(stack[:])
            else:
                helper(root.left,acc)
                helper(root.right,acc)
            acc -= stack.pop()


        helper(root,0)
        return result









a = Solution()


node = TreeNode(5)
node.left = TreeNode(4)
node.right = TreeNode(8)
node.left.left = TreeNode(11)
node.left.left.left = TreeNode(7)
node.left.left.right = TreeNode(2)
node.right.left = TreeNode(13)
node.right.right = TreeNode(4)
node.right.right.left = TreeNode(5)
node.right.right.right = TreeNode(1)

print(a.pathSum(node,22))