# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        if abs(left_depth - right_depth) > 1:
            return False
        return (self.isBalanced(root.left) and self.isBalanced(root.right))
    
    def getDepth(self, node):
        if node is None:
            return 0
        return 1 + max(self.getDepth(node.right), self.getDepth(node.left))