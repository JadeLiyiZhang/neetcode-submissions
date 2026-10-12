class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        mapping = defaultdict(list)
        indegree = defaultdict(int)
        for char in words:
            for i in range(len(char)):
                if char[i] not in indegree:
                    indegree[char[i]] = 0

        for i in range(1, len(words)):
            prev = words[i -1]
            cur = words[i]
            shorter = min(len(prev), len(cur))
            # shorter word can not be in the front of longer word if the shorter word is the prefix of the longer one
            if len(prev) > len(cur) and prev.startswith(cur):
                return ""
            
            for j in range(shorter):
                if prev[j] != cur[j]:
                    mapping[prev[j]].append(cur[j])
                    indegree[cur[j]] += 1
                    break
        seq = ''
        q = deque([])
        for key, value in indegree.items():
            if value == 0:
                q.append(key)
        
        while q:
            cur = q.popleft()
            seq += cur
            for nei in mapping[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(seq) != len(indegree):
            return ""
        
        return seq