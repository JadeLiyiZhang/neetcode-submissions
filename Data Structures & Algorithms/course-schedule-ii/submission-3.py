class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mapping = defaultdict(list)
        indegree = [0] * numCourses
        for after, pre in prerequisites:
            mapping[pre].append(after)
            indegree[after] += 1
        
        q = deque([])
        path = []
        visited = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            cur = q.popleft()
            if cur not in visited:
                visited.append(cur)
                for nei in mapping[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
        
        if len(visited) == numCourses:
            return visited
        
        else:
            return []
