class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        res = []
        for num in nums:
            map[num] = map.get(num, 0) + 1
        sorted_items = sorted(list(map.items()),key = lambda x: x[1], reverse = True)
        for i in range(k):
            res.append(sorted_items[i][0])
        return res