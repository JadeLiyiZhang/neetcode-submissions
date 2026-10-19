from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        @lru_cache(None)
        def dfs(start, cur_sum):
            if cur_sum == target:
                return True
            if cur_sum > target:
                return False
            if start == len(nums):
                return False
            return (dfs(start + 1, cur_sum) or dfs(start + 1, cur_sum + nums[start]))
        
        return dfs(0, 0)