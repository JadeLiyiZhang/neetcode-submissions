class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mapping = defaultdict(list)
        for start, end, cost in flights:
            mapping[start].append((end, cost))
        
        # dp[i][j]: the minimum cost to stop j using i steps
        dp = [[float('inf')] * (n) for _ in range(k + 2)]
        dp[0][src] = 0
        
        # heap <- cost, step, stop
        heap = [(0, 0, src)]
        
        while heap:
            cur_cost, cur_step, node = heapq.heappop(heap)

            if node == dst:
                return cur_cost
            
            if cur_cost > dp[cur_step][node]:
                continue
            
            for nei, cost in mapping[node]:
                next_cost = cur_cost + cost
                next_step = cur_step + 1
                if next_step > k + 1:
                    continue
                if next_cost < dp[next_step][nei]:
                    heapq.heappush(heap, (next_cost, next_step, nei))
                    dp[next_step][nei] = next_cost
        
        return -1


