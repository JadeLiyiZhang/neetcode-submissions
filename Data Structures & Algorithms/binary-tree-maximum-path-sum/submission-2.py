class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # 路径在当前节点连接左右两侧
            max_sum = max(max_sum, left + node.val + right)

            # 返回给父节点时，只能选择一侧；负贡献则舍弃
            return max(0, node.val + max(left, right))

        dfs(root)
        return max_sum