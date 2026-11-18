class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        mapping = {}
        start = 0
        res = float('-inf')
        for i, char in enumerate(s):
            if char in mapping and mapping[char] >= start:
                start = mapping[char] + 1
            res = max(res, i - start + 1)
            mapping[char] = i
        return res