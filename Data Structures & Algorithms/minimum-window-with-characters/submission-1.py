class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        left = 0
        valid = 0

        table_t = defaultdict(int)
        for char in t:
            table_t[char] += 1

        count = float('inf')
        res = ''

        for right in range(len(s)):
            char = s[right]
            if char in table_t:
                table_t[char] -= 1
                if table_t[char] == 0:
                    valid += 1

            while valid == len(table_t):
                cur_count = right - left + 1
                if cur_count < count:
                    count = cur_count
                    res = s[left: right + 1]
                outgoing = s[left]
                if outgoing in table_t:
                    if table_t[outgoing] == 0:
                        valid -= 1
                    table_t[outgoing] += 1
                left += 1
        if count == float('inf'):
            return ''
                
        return res
