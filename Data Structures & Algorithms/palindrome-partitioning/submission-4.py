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

        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s[i:j + 1]):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return res
