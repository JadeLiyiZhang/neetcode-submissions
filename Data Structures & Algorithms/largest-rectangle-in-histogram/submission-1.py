class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = float('-inf')
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                ans = max(ans, h * (i - index))
                start = index
            stack.append((start, height))
        
        for i, h in stack:
            ans = max(ans, h * (len(heights) - i))
        return ans