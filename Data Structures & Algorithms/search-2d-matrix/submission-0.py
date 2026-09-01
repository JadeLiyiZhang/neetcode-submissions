class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            left, right = 0, col - 1
            while left <= right:
                mid = left +((right - left) // 2)
                if matrix[i][mid] < target:
                    left = mid + 1
                if matrix[i][mid] > target:
                    right = mid - 1
                if matrix[i][mid] == target:
                    return True
        return False