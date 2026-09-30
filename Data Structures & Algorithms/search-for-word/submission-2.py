class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = [[0] * col for _ in range(row)]
        def backtracking(index, x, y):
            if index == len(word):
                return True
            if x < 0 or x >= row or y < 0 or y >= col:
                return False

            if board[x][y] != word[index]:
                return False
            
            if visited[x][y]:
                return False
            
            visited[x][y] = True

            
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            if board[x][y] == word[index]:
                for i, j in directions:
                    new_x, new_y = x + i, y + j
                    if backtracking(index + 1, new_x, new_y):
                        visited[x][y] = False
                        return True
            
            visited[x][y] = False
            return False

        
        for i in range(row):
            for j in range(col):
                if backtracking(0, i ,j):
                    return True
        
        return False