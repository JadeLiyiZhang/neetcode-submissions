class Solution:
    def checkValidString(self, s: str) -> bool:
        storage = []
        stars = []
        for i, char in enumerate(s):
            if char == '(':
                storage.append(i)
            if char == '*':
                stars.append(i)
            if char == ')':
                if storage:
                    storage.pop()
                else:
                    if stars:
                        stars.pop()
                    else:
                        return False
        
        while storage:
            if stars:
                if storage[-1] > stars[-1]:
                    return False
                else:
                    storage.pop()
                    stars.pop()
            else:
                return False

        return True  