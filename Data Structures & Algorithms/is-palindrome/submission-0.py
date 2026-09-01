class Solution:
    def isPalindrome(self, s: str) -> bool:
        store = []
        s = s.lower()
        print(s)
        for char in s:
            if 'a' <= char <= 'z' or '0' <= char <= '9':
                store.append(char)
        s_ = ''.join(store)
        return s_ == s_[::-1] 