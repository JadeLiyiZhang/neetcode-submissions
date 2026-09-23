class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '[': ']', '{': '}'}
        storage = []
        for p in s:
            if p in "({[":
                storage.append(p)
            else:
                if not storage:
                    return False
                last = storage.pop()
                if mapping[last] != p:
                    return False
        return True if not storage else False
