"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}

        def copyNode(node):
            if node in oldToNew:
                return oldToNew[node]
            
            if not node:
                return
            
            new_node = Node(node.val)
            oldToNew[node] = new_node
            new_node.next = copyNode(node.next)
            new_node.random = copyNode(node.random)
            return new_node
        
        return copyNode(head)