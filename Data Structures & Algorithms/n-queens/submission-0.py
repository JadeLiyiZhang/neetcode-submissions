class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        def dfs(r):
            if r == n:
                ans = ["".join(row) for row in board]
                res.append(ans)
                return
            
            for c in range(n):
                if self.safe(r, c, board):
                    board[r][c] = 'Q'
                    dfs(r + 1)
                    board[r][c] = '.'
        
        dfs(0)
        return res


    def safe(self, i, j, board):
        n = len(board)
        for k in range(n):
            if board[i][k] == "Q":
                return False
            if board[k][j] == "Q":
                return False
        
        directions = [[-1, -1], [1, 1], [-1, 1], [1, -1]]
        for x, y in directions:
            new_i, new_j = i + x, j + y
            while 0 <= new_i < n and 0 <= new_j < n:
                if board[new_i][new_j] == "Q":
                    return False
                new_i += x
                new_j += y
        return True



