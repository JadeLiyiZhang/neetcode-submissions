# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def helper(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            helper(node.left)
            helper(node.right)
            return
        
        helper(root)
        return ','.join(res)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_list = data.split(',')
        i = 0
        
        def dfs():
            nonlocal i
            if data_list[i] == 'N':
                i += 1
                return None
            node = TreeNode(int(data_list[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

                


