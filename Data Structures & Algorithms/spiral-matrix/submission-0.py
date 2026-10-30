class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []
        while top < bottom and left < right:
            # from left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # from top to bottom
            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1

            # from right to left
            for m in range(right, left - 1, -1):
                res.append(matrix[bottom][m])
            bottom -= 1

            # from bottom to top
            for n in range(bottom, top - 1, -1):
                res.append(matrix[n][left])
            left += 1
        
        if top == bottom and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
        
        elif left == right and top <= bottom:
            for i in range(top, bottom + 1):
                res.append(matrix[i][left])
        
        return res

