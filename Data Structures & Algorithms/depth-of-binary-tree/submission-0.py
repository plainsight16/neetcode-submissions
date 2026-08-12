# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 0
        depth = self.maxDepth(root.left)
        if depth > max_depth:
            max_depth = depth
        depth = self.maxDepth(root.right)
        if depth > max_depth:
            max_depth = depth
        return 1 + max_depth
        