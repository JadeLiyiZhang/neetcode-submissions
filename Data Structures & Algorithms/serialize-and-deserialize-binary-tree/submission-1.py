# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        path = []
        def dfs(node):
            if not node:
                path.append('N')
                return
            path.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(path)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        values = data.split(',')
        i = 0
        
        def dfs():
            nonlocal i
            value = values[i]
            i += 1
            if value == 'N':
                return None
            else:
                node = TreeNode(int(value))
                node.left = dfs()
                node.right = dfs()
            return node
        
        return dfs()


