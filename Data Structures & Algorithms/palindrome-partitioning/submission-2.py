class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                if s[left] == s[right]:
                    left += 1
                    right -= 1
            return True

        n = len(s)
        map = {}
        for start in reversed(range(n + 1)):
            map[start] = []
            for end in range(start + 1, n + 1):
                if isPalindrome(s[start:end]):
                    for item in map[end]:
                        map[start].append([s[start:end]] + item)
                    if end == n:
                        map[start].append([s[start:end]])
        return map[0]