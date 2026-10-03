from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            q = deque(visited)

            while q:
                r, c = q.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < row
                        and 0 <= nc < col
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return visited

        # 太平洋：上边界、左边界
        pacific = bfs(
            [(0, c) for c in range(col)]
            + [(r, 0) for r in range(row)]
        )

        # 大西洋：下边界、右边界
        atlantic = bfs(
            [(row - 1, c) for c in range(col)]
            + [(r, col - 1) for r in range(row)]
        )

        return [
            [r, c]
            for r in range(row)
            for c in range(col)
            if (r, c) in pacific and (r, c) in atlantic
        ]