class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mapping = defaultdict(list)
        for a, b in edges:
            mapping[a].append(b)
            mapping[b].append(a)
        
        def has_cycle(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for nei in mapping[node]:
                if nei == parent:
                    continue
                if has_cycle(nei, node):
                    return True
            return False
        visited = set()
        if has_cycle(0, -1):
            return False
        if len(visited) == n:
            return True
        return False