# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = float('-inf')
        def helper(node):
            nonlocal res
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            res = max(res, node.val + left + right)
            return max(0, node.val + left, node.val + right)
        
        helper(root)
        return res
