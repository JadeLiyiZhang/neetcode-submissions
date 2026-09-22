class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        left_max = 0
        for i in range(len(height)):
            left[i] = left_max
            left_max = max(left_max, height[i])
        right_max = 0
        for i in range(len(height) -1, -1, -1):
            right[i] = right_max
            right_max = max(right_max, height[i])
        res = 0
        for i in range(len(height)):
            res += max(0, (min(left[i], right[i]) - height[i]))
        return res