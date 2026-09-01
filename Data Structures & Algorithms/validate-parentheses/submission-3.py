class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {'(': ')', '[': ']', '{': '}'}
        for i in range(len(s)):
            if s[i] in table:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                pair = stack.pop()
                if table[pair] != s[i]:
                    return False
        if stack:
            return False
        return True