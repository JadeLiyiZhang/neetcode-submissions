class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.minHeap or num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        while len(self.maxHeap) > len(self.minHeap) - 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        
        while len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))


    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return  (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            return self.minHeap[0]