class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = []
        cur_start = intervals[0][0]
        cur_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start <= cur_end:
                cur_end = max(end, cur_end)
            else:
                res.append([cur_start, cur_end])
                cur_start = start
                cur_end = end
        res.append([cur_start, cur_end])
        return res