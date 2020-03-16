"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        if root is None:
            return []
        elif not root.children:
            return [root.val]
        else:
            result = [root.val]
            for subtree in root.children:
                result.extend(self.preorder(subtree))
            return result