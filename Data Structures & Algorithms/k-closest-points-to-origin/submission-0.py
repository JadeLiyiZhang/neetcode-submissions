class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            d = x * x + y * y
            if len(heap) < k:
                heapq.heappush(heap, (-d, (x, y)))
            else:
                if d < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-d, (x, y)))
        res = []
        for d, (x, y) in heap:
            res.append([x, y])
        return res