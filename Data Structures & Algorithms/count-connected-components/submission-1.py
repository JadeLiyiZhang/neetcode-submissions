class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mapping = defaultdict(list)
        for a, b in edges:
            mapping[a].append(b)
            mapping[b].append(a)
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in mapping[node]:
                if nei in visited:
                    continue
                dfs(nei)
        res = 0
        for  i in range(n):
            if i in visited:
                continue
            dfs(i)
            res += 1
        return res