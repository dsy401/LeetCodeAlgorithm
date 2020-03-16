# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        arr = []
        def helper(root):
            if root:
                if root.val !=None:
                    arr.append(root.val)
                helper(root.left)
                helper(root.right)

        helper(root)


        sum = 0

        for val in arr:
            if val >= L and val <= R:
                sum += val

        return sum





t = TreeNode(10)
t.left = TreeNode(5)
t.right = TreeNode(15)
t.left.left = TreeNode(3)
t.left.right = TreeNode(7)
t.right.left = TreeNode(None)
t.right.right = TreeNode(18)

a = Solution()
print(a.rangeSumBST(t,7,15))