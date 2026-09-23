class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        table_s1 = [0] * 26
        for char in s1:
            table_s1[ord(char) - ord('a')] += 1
        window_size = len(s1)
        table_s2 = [0] * 26
        for char in s2[:window_size]:
            table_s2[ord(char) - ord('a')] += 1
        if table_s2 == table_s1:
            return True
        for start in range(1, len(s2) - window_size + 1):
            table_s2[ord(s2[start - 1]) - ord('a')] -= 1
            table_s2[ord(s2[start + window_size - 1]) - ord('a')] += 1
            if table_s1 == table_s2:
                return True
        return False