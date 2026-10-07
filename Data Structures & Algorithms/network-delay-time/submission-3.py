class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mapping = defaultdict(list)
        for start, end, cost in times:
            mapping[start].append((end, cost))
        
        cur_time = 0
        heap = [(0, k)]
        visited = [float('inf')] * (n + 1)
        visited[k] = 0
        while heap:
            time, stop = heapq.heappop(heap)
            if time != visited[stop]:
                continue
            
            for nei, cost in mapping[stop]:
                next_time = time + cost
                if next_time < visited[nei]:
                    heapq.heappush(heap, (next_time, nei))
                    visited[nei] = min(visited[nei], next_time)
        ans = float('-inf')
        for time in visited[1:]:
            if time == float('inf'):
                return -1
            ans = max(ans, time)
        return ans