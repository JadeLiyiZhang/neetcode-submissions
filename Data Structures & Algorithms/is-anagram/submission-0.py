class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}
        for car in s:
            table[car] = table.get(car, 0) + 1
        for car in t:
            if car not in table:
                return False
            table[car] -= 1
        for key in table.values():
            if key != 0:
                return False
        return True