# Last updated: 8/15/2026, 3:05:47 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0
        
        return 1 +  self.countNodes(root.left) + self.countNodes(root.right)
        