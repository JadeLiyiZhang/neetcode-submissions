# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxval):
            if node is None:
                return 0
            if node.val >= maxval:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            if node.val < maxval:
                return dfs(node.left, maxval) + dfs(node.right, maxval)
        return dfs(root, root.val)