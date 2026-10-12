"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        heap = []
        for interval in intervals:
            start, end = interval.start, interval.end
            heapq.heappush(heap, (start, end))
        
        cur_start, cur_end = heapq.heappop(heap)
        while heap:
            start, end = heapq.heappop(heap)
            if start < cur_end:
                return False
            cur_end = end
        return True
