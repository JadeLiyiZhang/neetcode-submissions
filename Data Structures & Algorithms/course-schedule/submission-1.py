class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = defaultdict(list)
        indegree = [0] * numCourses
        for after, before in prerequisites:
            mapping[before].append(after)
            indegree[after] += 1
        
        q = deque()
        completed = 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            completed += 1
            for neighbor in mapping[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return completed == numCourses