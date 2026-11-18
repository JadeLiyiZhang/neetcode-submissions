# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=, Mapping0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {num: index for index, num in enumerate(inorder)}
        pre_index = 0

        def helper(l, r):
            nonlocal pre_index
            if l > r:
                return None
            root_val = preorder[pre_index]
            pre_index += 1
            
            root = TreeNode(root_val)
            inorder_index = inorder_map[root_val]

            root.left = helper(l, inorder_index - 1)
            root.right = helper(inorder_index + 1, r)

            return root
        return helper(0, len(inorder) - 1)



