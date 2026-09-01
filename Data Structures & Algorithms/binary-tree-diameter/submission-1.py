# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_path = self.maxDepth(root.left)
        right_path = self.maxDepth(root.right)
        diameter = left_path + right_path
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)
        
    def maxDepth(self, node):
        if node is None:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))