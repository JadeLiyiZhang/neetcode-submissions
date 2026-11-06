class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for string in strs:
            encode.append(str(len(string)))
            encode.append('#')
            encode.append(string)
        return ''.join(encode)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            ans.append(s[j + 1:j+ 1 + length])
            i = j + length + 1
        return ans


