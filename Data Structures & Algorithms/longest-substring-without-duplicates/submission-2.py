class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapping = {}
        res = 0
        start = 0
        for i, char in enumerate(s):
            if char in mapping and mapping[char] >= start:
                start = mapping[char] + 1
            mapping[char] = i
            res = max(res, i - start + 1)
        return res