class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        table = [0] * (len(nums) + 1)
        for num in nums:
            if table[num] >= 1:
                return num
            table[num] += 1
        return None