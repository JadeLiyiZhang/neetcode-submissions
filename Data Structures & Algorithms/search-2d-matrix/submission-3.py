class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        top, bottom = 0, row - 1
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        res_row = None
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                res_row = mid
                top = mid + 1
            else:
                bottom = mid - 1
        
        
        left, right = 0, col - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[res_row][mid] == target:
                return True
            elif matrix[res_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
            