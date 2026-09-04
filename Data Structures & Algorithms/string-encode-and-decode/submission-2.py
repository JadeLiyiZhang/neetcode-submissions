class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append('#')
            res.append(word)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            len_cur = int(s[i:j])
            res.append(s[j + 1 : j + len_cur + 1])
            i = j + len_cur + 1
        return res

