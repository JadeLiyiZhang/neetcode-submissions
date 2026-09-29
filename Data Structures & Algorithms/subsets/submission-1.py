class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(path, start):
            if start > len(nums):
                return
            
            res.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(path, i + 1)
                path.pop()
        
        backtracking([], 0)
        return res