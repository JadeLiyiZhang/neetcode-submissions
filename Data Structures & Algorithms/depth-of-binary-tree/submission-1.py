# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left_path = self.maxDepth(root.left)
        right_path = self.maxDepth(root.right)
        return left_path + right_path

    def maxDepth(self, node):
        if node is None:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))