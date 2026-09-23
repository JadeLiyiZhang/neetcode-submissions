class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        left = 0
        window = {}
        valid = 0
        min_len = float('inf')
        answer_start = 0

        for right in range(len(s)):
            if s[right] in t:
                window[s[right]] = window.get(s[right], 0) + 1
                if window[s[right]] == need[s[right]]:
                    valid += 1

            while valid == len(need):
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    answer_start = left
                
                left_char = s[left]
                if left_char in need:
                    if window[left_char] == need[left_char]:
                        valid -= 1
                    window[left_char] -= 1
                left += 1

        if min_len == float('inf'):
            return ''
        return s[answer_start: answer_start + min_len]
