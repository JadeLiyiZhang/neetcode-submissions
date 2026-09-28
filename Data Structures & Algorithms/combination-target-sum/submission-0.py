class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(cur_sum, path, start):
            if cur_sum == target:
                res.append(path.copy())
                return
            if cur_sum > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                cur_sum += nums[i]
                backtracking(cur_sum, path, i)
                path.pop()
                cur_sum -= nums[i]
            
        backtracking(0, [], 0)
        return res