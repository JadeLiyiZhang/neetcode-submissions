class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        l = 0
        r = l + s1_len - 1
        list_1 = [0] * 26
        for char in s1:
            list_1[ord(char) - ord('a')] += 1

        while l <= len(s2) - len(s1):
            list_2 = [0] * 26
            for i in range(l, l + len(s1)):
                list_2[ord(s2[i]) - ord('a')] += 1
            if list_2 == list_1:
                return True
            l += 1
        return False