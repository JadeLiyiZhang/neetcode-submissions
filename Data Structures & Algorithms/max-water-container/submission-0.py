class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = float('-inf')
        while left < right:
            vol = min(heights[right], heights[left]) * (right - left)
            res= max(res, vol)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return res