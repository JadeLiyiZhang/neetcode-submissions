class Solution:
    def isHappy(self, n: int) -> bool:
        cur_sum = 0
        seen = set()
        while n:
            total = 0
            for i in range(len(str(n))):
                d, m = divmod(n, 10)
                total += m * m
                n = d
            if total == 1:
                return True
            elif total in seen:
                return False
            seen.add(total)
            n = total
        return False
