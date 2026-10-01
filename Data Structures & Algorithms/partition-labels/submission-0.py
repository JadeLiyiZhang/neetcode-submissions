class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = [-1] * 26
        end = [-1] * 26
        for i in range(len(s)):
            if start[ord(s[i]) - ord('a')] == -1:
                start[ord(s[i]) - ord('a')] = i
            
            end[ord(s[i]) - ord('a')] = i
        
        intervals = []
        for j in range(26):
            if start[j] == -1:
                continue
            intervals.append([start[j], end[j]])
        intervals.sort()
        res = []
        cur_start = intervals[0][0]
        cur_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < cur_end:
                cur_end = max(end, cur_end)
            else:
                res.append([cur_start, cur_end])
                cur_start = start
                cur_end = end
        res.append([cur_start, cur_end])
        ans = []
        for m, n in res:
            ans.append(n - m + 1)
        return ans
