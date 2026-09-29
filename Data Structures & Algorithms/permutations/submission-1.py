class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(path, visited):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if visited[i] == True:
                    continue
                path.append(nums[i])
                visited[i] = True
                backtracking(path, visited)
                visited[i] = False
                path.pop()

        backtracking([], [False] * len(nums))
        return res