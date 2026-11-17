# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(lower, higher, node):
            if not node:
                return True
            if not lower < node.val < higher:
                return False
            return helper(lower, node.val, node.left) and helper(node.val, higher, node.right)
        
        return helper(float('-inf'), float('inf'), root)