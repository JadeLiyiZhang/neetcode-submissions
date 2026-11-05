class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = [0] * 26
        for char in s:
            table[ord(char) - ord('a')] += 1
        for char in t:
            table[ord(char) - ord('a')] -= 1
        
        for count in table:
            if count != 0:
                return False
        return True
