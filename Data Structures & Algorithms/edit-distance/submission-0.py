class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # dp[i][j]: steps take to match word1[i:] and word2[j:]
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(m + 1):
            dp[i][n] = m - i
        
        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    # delete or insert
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

        return dp[0][0]