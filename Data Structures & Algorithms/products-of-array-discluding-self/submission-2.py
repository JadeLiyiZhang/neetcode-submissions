class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefix = [1] * len(nums)
        right_prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            left_prefix[i] = left_prefix[i - 1] * nums[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            right_prefix[j] = right_prefix[j + 1] * nums[j + 1]
        for m in range(len(nums)):
            right_prefix[m] = right_prefix[m] * left_prefix[m]
        return right_prefix