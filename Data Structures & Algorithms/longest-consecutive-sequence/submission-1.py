class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(nums)
        res = 1
        count = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue
            elif nums[i + 1] == nums[i] + 1:
                count += 1
                res = max(res, count)
            else:
                count = 1
        return res
            