# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, upper_bound, lower_bound):
            if not node:
                return True
            if lower_bound < node.val < upper_bound:
                return helper(node.left, node.val, lower_bound) and helper(node.right, upper_bound, node.val)
            return False
        
        return helper(root, float('inf'), float('-inf'))