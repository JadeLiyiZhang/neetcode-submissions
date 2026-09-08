class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    while left + 1 < len(nums) and nums[left + 1] == nums[left]:
                        left += 1
                    while right > 0 and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                if cur_sum < target:
                    left += 1
                if cur_sum > target:
                    right -= 1
        return res
                
                