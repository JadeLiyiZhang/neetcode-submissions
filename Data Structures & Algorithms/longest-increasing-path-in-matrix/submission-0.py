class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[1] * col for _ in range(row)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        cells = []
        for i in range(row):
            for j in range(col):
                cells.append((matrix[i][j], i, j))
        cells.sort()

        for value, i, j in cells:
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < row and 0 <= new_j < col and matrix[new_i][new_j] > matrix[i][j]:
                    dp[new_i][new_j] = max(dp[new_i][new_j], dp[i][j] + 1)
        res = 1
        for i in range(row):
            for j in range(col):
                res = max(res, dp[i][j])
        return res