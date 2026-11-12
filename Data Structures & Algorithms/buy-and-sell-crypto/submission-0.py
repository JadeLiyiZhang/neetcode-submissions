class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        max_profit = float('-inf')
        for i in range(len(prices)):
            if prices[i] < prices[start]:
                start = i
            else:
                max_profit = max(max_profit, prices[i] - prices[start])
        return max_profit