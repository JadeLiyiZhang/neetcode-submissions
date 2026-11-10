class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in num_set:
                lengh = 1
                while num + 1 in num_set:
                    lengh += 1
                    num = num + 1
                res = max(res, lengh)
        return res