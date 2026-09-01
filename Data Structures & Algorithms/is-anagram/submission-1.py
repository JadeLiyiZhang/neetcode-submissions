class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table_s = [0]* 26
        for char in s:
            table_s[ord(char) - ord('a')] += 1
        for i in t:
            table_s[ord(i) - ord('a')] -= 1
        for k in table_s:
            if k != 0:
                return False
        return True