class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for num in digits:
            res = res * 10 + num
        res += 1
        ans = []
        while res:
            d, m = divmod(res, 10)
            ans.append(m)
            res = d
        ans.reverse()
        return ans