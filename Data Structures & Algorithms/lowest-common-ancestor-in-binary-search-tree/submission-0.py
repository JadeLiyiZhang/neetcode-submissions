# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not q or not p:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, q, p)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, q, p)
        else:
            return root