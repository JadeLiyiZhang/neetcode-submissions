class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(path, start):
            if start > len(nums):
                return
            
            res.append(path.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                backtracking(path, i + 1)
                path.pop()
        
        backtracking([], 0)
        return res