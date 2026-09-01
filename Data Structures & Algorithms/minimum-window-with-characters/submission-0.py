class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        table, window = {}, {}
        for char in t:
            table[char] = table.get(char, 0) + 1

        have, need = 0, len(table)
        res, reslen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in table and window[c] == table[c]:
                have += 1

            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                window[s[l]] -= 1

                if s[l] in table and window[s[l]] < table[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l : r + 1] if reslen != float("infinity") else ""