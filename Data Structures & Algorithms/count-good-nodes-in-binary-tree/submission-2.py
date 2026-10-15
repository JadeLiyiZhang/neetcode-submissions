# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def helper(node, bound):
            nonlocal res
            if not node:
                return
            if node.val >= bound:
                res += 1
            helper(node.left, max(bound, node.val))
            helper(node.right, max(bound, node.val))
        
        helper(root, float('-inf'))
        return res