class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        res = False
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 0
        list_ = list(map.values())
        for i in list_:
            if i != 0:
                res = True
        return res