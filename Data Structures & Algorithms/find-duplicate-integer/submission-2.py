class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapping = {}
        for num in nums:
            if num in mapping:
                return num
            mapping[num] = 1
        return -1