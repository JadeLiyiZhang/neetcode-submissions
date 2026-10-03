class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        def dfs(x, y):
            if x < 0 or x >= row or y < 0 or y >= col or board[x][y] != 'O':
                return
            
            board[x][y] = '1'
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
        
        for j in range(col):
            if board[0][j] == 'O':
                dfs(0, j)
        
            if board[row - 1][j] == "O":
                dfs(row - 1, j)
        
        for i in range(row):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][col - 1] == "O":
                dfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '1':
                    board[i][j] = 'O'