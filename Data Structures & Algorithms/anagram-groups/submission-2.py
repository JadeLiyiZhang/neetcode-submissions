class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        combinations = defaultdict(list)
        for word in strs:
            char_table = [0] * 26
            for char in word:
                char_table[(ord(char) - ord('a'))] += 1
            combinations[tuple(char_table)].append(word)
        res = []
        for key, value in combinations.items():
            res.append(value)
        return res