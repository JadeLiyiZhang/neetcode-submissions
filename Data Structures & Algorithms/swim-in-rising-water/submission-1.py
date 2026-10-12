class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        #dp[x][y]: the minimum water level that can reach this grid
        dp = [[float("inf")] * col for _ in range(row)]
        dp[0][0] = grid[0][0]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # time, x, y
        heap = [(grid[0][0], 0, 0)]
        while heap:
            time, x, y = heapq.heappop(heap)
            
            if time > dp[x][y]:
                continue
            
            if x == row - 1 and y == col - 1:
                return time
            
            for i, j in directions:
                new_x, new_y = x + i, y + j
                if 0 <= new_x < row and 0 <= new_y < col:
                    new_time = max(time, grid[new_x][new_y])

                    if new_time < dp[new_x][new_y]:
                        heapq.heappush(heap, (new_time, new_x, new_y))
                        dp[new_x][new_y] = new_time
        

