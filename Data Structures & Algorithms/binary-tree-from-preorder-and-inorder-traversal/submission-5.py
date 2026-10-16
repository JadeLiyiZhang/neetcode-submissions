# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        
        cur = 0
        
        def dfs(left, right):
            nonlocal cur
            if left > right:
                return None
            node_val = preorder[cur]
            cur += 1
            node = TreeNode(node_val)
            
            i = indices[node_val]
            node.left = dfs(left, i - 1)
            node.right = dfs(i + 1, right)
        
            return node
        
        return dfs(0, len(preorder) - 1)