class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        for x, y in self.points.keys():
            if (qx, y) in self.points and (x, qy) in self.points:
                if abs(qx - x) != abs(qy - y) or qx  == x or qy == y:
                    continue
                res += self.points[(x, y)] * self.points[(qx, y)] * self.points[(x, qy)]
        return res