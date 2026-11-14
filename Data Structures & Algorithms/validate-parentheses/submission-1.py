class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(": ')', "{": "}", "[": "]"}
        for p in s:
            if p in '({[':
                stack.append(p)
            else:
                if not stack:
                    return False
                if p != mapping[stack.pop()]:
                    return False
        if not stack:
            return True
        return False

