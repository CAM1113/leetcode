from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 2:
            return True
        x0y0 = coordinates[0]
        x1y1 = coordinates[1]
        dx = x1y1[0] - x0y0[0]
        dy = x1y1[1] - x0y0[1]
        if dx == 0:
            # y = a
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != x0y0[0]:
                    return False
            return True

        if dy == 0:
            # x = a
            for i in range(2, len(coordinates)):
                if coordinates[i][1] != x0y0[1]:
                    return False
            return True

        k = dy / dx
        b = x0y0[1] - k * x0y0[0]
        for i in range(2, len(coordinates)):
            if coordinates[i][1] != k * coordinates[i][0] + b:
                return False
        return True
