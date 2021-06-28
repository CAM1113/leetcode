import collections
from typing import List


def get_kb(p1, p2):
    if p2[0] == p1[0]:
        return None, p2[0]
    k = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - k * p1[0]
    return k, b


def is_on_line(k, b, p):
    if k is None:
        return b == p[0]
    return abs(p[1] - (k * p[0] + b)) < 1e-10


def solve_kb(k, b, line_dict, j, points: List[List[int]]):
    key = f"{k}-{b}"
    line_dict[key] = 2
    for index in range(j + 1, len(points)):
        p = points[index]
        if is_on_line(k, b, p):
            print(f"{p} on {k} {b}")
            line_dict[key] += 1


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        line_dict = collections.defaultdict(int)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]
                k, b = get_kb(p1, p2)
                kb = f"{k}-{b}"
                if kb in line_dict.keys():
                    print(f"kb={kb},continue")
                    continue
                solve_kb(k, b, line_dict, j, points)
        return max(line_dict.values())


if __name__ == '__main__':
    x = [[-184, -551], [-105, -467], [-90, -394], [-60, -248], [115, 359], [138, 429], [60, 336], [150, 774],
         [207, 639], [-150, -686], [-135, -613], [92, 289], [23, 79], [135, 701], [0, 9], [-230, -691], [-115, -341],
         [-161, -481], [230, 709], [-30, -102]]
    print(Solution().maxPoints(x))
