"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def cloneNode(node):
            if not node:
                return
            if node in oldToNew:
                return oldToNew[node]
            
            newNode = Node(val=node.val)
            oldToNew[node] = newNode
            for nei in node.neighbors:
                newNode.neighbors.append(cloneNode(nei))
            return newNode
            
        return cloneNode(node)