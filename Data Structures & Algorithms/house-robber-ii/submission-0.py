class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(left, right):
            if left == right:
                return nums[left]
            
            nums_part = nums[left:right + 1]
            dp = [0] * len(nums_part)
            dp[0] = nums_part[0]
            dp[1] = max(nums_part[0], nums_part[1])
            for i in range(2, len(nums_part)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums_part[i])
            return dp[len(nums_part) - 1]

        exclude_last = helper(0, len(nums) - 2)
        exclude_first = helper(1, len(nums) - 1)
        return max(exclude_first, exclude_last)