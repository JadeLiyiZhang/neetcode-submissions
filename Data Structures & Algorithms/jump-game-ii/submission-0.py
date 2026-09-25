class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        cur_max = 0
        next_max = 0
        for i in range(len(nums) - 1):
            next_max = max(next_max, i + nums[i])
            if i == cur_max:
                step += 1
                cur_max = next_max
        return step
        