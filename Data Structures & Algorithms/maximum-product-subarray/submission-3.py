class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[num for num in nums] for i in range(2)]
        for i in range(1, len(nums)):
            dp[0][i] = max(dp[0][i], dp[0][i - 1] * nums[i], dp[1][i - 1] * nums[i])
            dp[1][i] = min(dp[1][i], dp[0][i - 1] * nums[i], dp[1][i - 1] * nums[i])
        res = float('-inf')
        for i in range(2):
            for j in range(len(nums)):
                res = max(res, dp[i][j])
        return res

