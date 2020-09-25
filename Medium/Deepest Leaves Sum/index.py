# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        result = {}

        def find(root, level):
            if root != None:
                find(root.left, level + 1)
                find(root.right, level + 1)
                if level not in result:
                    result[level] = [root.val]
                else:
                    result[level].append(root.val)

        find(root,0)
        max=0
        for key in result:
            if key > max:
                max = key


        return sum(result[max])





a = Solution()

node = TreeNode(6)
node.left = TreeNode(7)
node.right = TreeNode(8)
node.left.left = TreeNode(2)
node.left.right =TreeNode(7)
node.right.left = TreeNode(1)
node.right.right = TreeNode(3)
node.left.left.left = TreeNode(9)

node.left.right.left =TreeNode(1)
node.left.right.right = TreeNode(4)

node.right.right.right = TreeNode(5)
print(a.deepestLeavesSum(node))