class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        
        def backtracking(i, j, index):
            if index == len(word):
                return True
            
            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != word[index]:
                return False
            
            origin = board[i][j]
            board[i][j] = '*'
            
            found = (backtracking(i + 1, j, index + 1) or
                backtracking(i - 1, j, index + 1) or
                backtracking(i, j + 1, index + 1) or
                backtracking(i, j - 1, index + 1))
            
            board[i][j] = origin
            return found
            
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if backtracking(i, j, 0):
                        return True
        return False
            

