class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def hoursNeed(speed):
            res = 0
            for pile in piles:
                res += math.ceil(pile / speed)
            return res
        ans = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            if hoursNeed(mid) <= h:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return ans


