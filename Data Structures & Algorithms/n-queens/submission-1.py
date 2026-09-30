class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = [['.'] * n for _ in range(n)]
        res = []
               
        def isSafe(r, c, board):
            row = r - 1
            while row >= 0:
                if board[row][c] == 'Q':
                    return False
                row -= 1
            
            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -=1
            
            row, col = r - 1, c + 1
            while row >= 0 and col < len(board):
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col += 1
            
            return True

        def backtracking(i):
            if i == n:
                res.append([''.join(row) for row in chessboard])
                return
            
            for j in range(n):
                # try to place Q in chessboard[i][j]
                if isSafe(i, j, chessboard):
                    chessboard[i][j] = 'Q'
                    backtracking(i + 1)
                    chessboard[i][j] = '.'
        
        backtracking(0)
        return res
