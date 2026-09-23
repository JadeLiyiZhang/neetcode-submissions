class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        table_s1 = [0] * 26
        for char in s1:
            table_s1[ord(char) - ord('a')] += 1
        window_size = len(s1)
        for start in range(len(s2) - window_size + 1):
            substring = s2[start:start + window_size]
            table_s2 = [0] * 26
            for char in substring:
                table_s2[ord(char) - ord('a')] += 1
            if table_s1 == table_s2:
                return True
        return False