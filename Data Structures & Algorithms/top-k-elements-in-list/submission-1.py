class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for num in nums:
            if num not in table:
                table[num] = 1
            else:
                table[num] += 1
        sorted_table = sorted(table.items(), key = lambda x: x[1], reverse=True)
        res = []
        for num, freq in sorted_table:
            res.append(num)
            k -= 1
            if k == 0:
                break
        return res