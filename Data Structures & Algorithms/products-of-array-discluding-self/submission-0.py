class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        proExpZero = 1
        noZero = 0
        for num in nums:
            if num == 0:
                noZero += 1
            if num != 0:
                proExpZero *= num
        if noZero == 0:
            res = []
            for num in nums:
                res.append(proExpZero // num)
        if noZero == 1:
            res = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = proExpZero
        if noZero > 1:
            res = [0] * len(nums)
        return res