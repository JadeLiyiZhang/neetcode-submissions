class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        q = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i, j))
        step = 1
        while q:
            cur_x, cur_y = q.popleft()
            for m, n in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_x, new_y = cur_x + m, cur_y + n
                if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == 2147483647:
                    grid[new_x][new_y] = grid[cur_x][cur_y] + 1
                    q.append((new_x, new_y))

            
            