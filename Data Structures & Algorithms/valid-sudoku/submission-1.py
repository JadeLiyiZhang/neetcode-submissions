class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        for i in range(row):
            seen = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        for m in range(col):
            visited = set()
            for n in range(9):
                if board[n][m] == '.':
                    continue
                if board[n][m] in visited:
                    return False
                visited.add(board[n][m])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True