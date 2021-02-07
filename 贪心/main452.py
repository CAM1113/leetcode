from typing import List


def is_cross(r1, r2):
    return r1[0] <= r2[0] <= r1[1] or r1[0] <= r2[1] <= r1[1]


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[0])
        ranges = [points[0]]
        for i in range(1, len(points)):
            p = points[i]
            r = ranges[-1]
            if r[0] <= p[0] <= r[1]:
                r[0] = p[0]
                r[1] = min(r[1], p[1])
            else:
                ranges.append(p)
        return len(ranges)


if __name__ == '__main__':
    points = [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
    print(Solution().findMinArrowShots(points))
