# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            rightSide = None
            n = len(queue)
            for i in range(n):
                temp = queue.popleft()
                if temp:
                    rightSide = temp
                    queue.append(temp.left)
                    queue.append(temp.right)
            if rightSide:
                res.append(rightSide.val)
        return res