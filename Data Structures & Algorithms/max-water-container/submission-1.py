class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            vol = (right - left) * min(heights[left], heights[right])
            res = max(res, vol)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res