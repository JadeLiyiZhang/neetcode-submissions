class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        str_1 = strs[0]
        str_2 = strs[-1]
        res = ''
        for i in range(min(len(str_1), len(str_2))):
            if str_1[i] == str_2[i]:
                res += str_1[i]
            else:
                return res
        return res