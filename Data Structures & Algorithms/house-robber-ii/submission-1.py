class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(left, right):
            if right - left + 1 == 1:
                return nums[left]
            temp_num = nums[left: right + 1]
            dp = [0] * len(temp_num)
            dp[0] = temp_num[0]
            dp[1] = max(temp_num[0], temp_num[1])
            for i in range(2, len(temp_num)):
                dp[i] = max(dp[i - 1], dp[i - 2] + temp_num[i])
            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]

        skip_last = helper(0, len(nums) - 2)
        skip_first = helper(1, len(nums) - 1)
        return max(skip_first, skip_last)