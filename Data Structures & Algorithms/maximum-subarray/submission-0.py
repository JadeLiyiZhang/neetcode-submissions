class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        res = float('-inf')
        for right in range(len(nums)):
            cur_sum += nums[right]
            res = max(res, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return res