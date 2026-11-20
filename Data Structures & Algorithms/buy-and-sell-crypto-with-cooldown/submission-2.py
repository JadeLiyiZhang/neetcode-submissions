class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][j]: the max profit get when sell or not sell on that day
        # j = 0: do not hold stock; j = 1: hold stock; j = 2: sell stock
        n = len(prices)
        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            # dp[i][0]: do not hold stock
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            # dp[i][1]: hold stock
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            # dp[i][2]: sell stock
            dp[i][2] = dp[i - 1][1] + prices[i]
        
        return max(dp[-1])


