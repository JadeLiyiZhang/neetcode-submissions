class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        k = 0
        for fast in range(len(nums)):
            if nums[fast] == val:
                continue
            else:
                nums[slow] = nums[fast]
                slow += 1
                k += 1
        return k