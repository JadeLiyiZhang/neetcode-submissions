class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        res = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                res = max(res, prices[right] - prices[left])
        return res