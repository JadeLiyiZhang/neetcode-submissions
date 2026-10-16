class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand_odd(x):
            left, right = x - 1, x + 1
            res = s[x]
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    res = s[left: right + 1]
                    left -= 1
                    right += 1
                else:
                    break
            return res
        
        def expand_even(y):
            res = s[y]
            left, right = y, y + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    res = s[left : right + 1]
                    left -= 1
                    right += 1
                else:
                    break
            return res

        ans = ''
        for i in range(len(s)):
            cur_1 = expand_odd(i)
            cur_2 = expand_even(i)
            if len(cur_1) > len(cur_2):
                if len(cur_1) > len(ans):
                    ans = cur_1
            else:
                if len(cur_2) > len(ans):
                    ans = cur_2
        return ans