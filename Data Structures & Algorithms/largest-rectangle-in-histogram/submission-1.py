class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        res = float('-inf')
        for i, height in enumerate(heights):
            if not s:
                s.append((i, height))
            else:
                if heights[i] >= s[-1][1]:
                    s.append((i, height))
                else:
                    while s and s[-1][1] >= height:
                        last_i, last_h = s.pop()
                        area = last_h * (i - last_i)
                        res = max(res, area)
                        start = last_i
                    s.append((start, height))
        for start, height in s:
            res = max(res, height * (len(heights) - start))
        return res
