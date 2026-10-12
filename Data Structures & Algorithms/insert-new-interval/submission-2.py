class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        cur_start = intervals[0][0]
        cur_end = intervals[0][1]
        
        res = []

        for start, end in intervals[1:]:
            if start <= cur_end:
                cur_end = max(cur_end, end)
            
            else:
                res.append([cur_start, cur_end])
                cur_start = start
                cur_end = end
        res.append([cur_start, cur_end])
        return res