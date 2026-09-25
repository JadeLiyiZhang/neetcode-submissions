class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len = nums[0]
        for i in range(len(nums)):
            if max_len < i:
                return False
            max_len = max(max_len, i + nums[i])
        return True