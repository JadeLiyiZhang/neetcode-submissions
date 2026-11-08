class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_left = [1] * len(nums)
        pre_right = [1] * len(nums)
        for i in range(1, len(nums)):
            pre_left[i] = pre_left[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            pre_right[i] = pre_right[i + 1] * nums[i + 1]
        res = []
        for i in range(len(nums)):
            res.append(pre_left[i] * pre_right[i])
        return res
