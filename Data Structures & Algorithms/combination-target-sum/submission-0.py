class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(start_index, cur_sum, path):
            if cur_sum == target:
                res.append(path.copy())
                return
            
            if cur_sum > target:
                return
            
            for i in range(start_index, len(nums)):
                cur_sum += nums[i]
                path.append(nums[i])
                backtracking(i, cur_sum, path)
                cur_sum -= nums[i]
                path.pop()
        
        backtracking(0, 0, [])
        return res