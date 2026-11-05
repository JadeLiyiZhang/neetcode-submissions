class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for s in strs:
            table_s = [0] * 26
            for char in s:
                table_s[ord(char) - ord('a')] += 1
            table[tuple(table_s)].append(s)
        return list(table.values())
