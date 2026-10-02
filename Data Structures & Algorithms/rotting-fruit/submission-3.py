class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = deque([])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i, j])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minites = 0
        while q:
            cur_x, cur_y = q.popleft()
            minites = grid[cur_x][cur_y] - 2
            for m, n in directions:
                new_x, new_y = cur_x + m, cur_y + n
                if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = grid[cur_x][cur_y] + 1
                    q.append([new_x, new_y])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        
        return minites