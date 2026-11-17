# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        res = None
        def helper(node):
            nonlocal res
            if res is not None:
                return 
            if not node:
                return 
            helper(node.left)
            nodes.append(node.val)
            if len(nodes) == k:
                res = node.val
            helper(node.right)
        
        helper(root)
        return res