class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        table = {}
        max_freq = 0
        ans = 0

        for right in range(len(s)):
            freq = table.get(s[right], 0) + 1
            table[s[right]] = freq
            if freq > max_freq:
                max_freq = freq
            while (right - left + 1) - max_freq > k:
                table[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans