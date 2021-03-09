from typing import List


def is_ok(a, b, c, d, e, f, g, h, i):
    v = a != b != c != d != e != f != g != h != i
    v = v and 0 < a < 10 and 0 < b < 10 and 0 < c < 10 and \
        0 < d < 10 and 0 < e < 10 and 0 < f < 10 and \
        0 < g < 10 and 0 < h < 10 and 0 < i < 10
    return v and a + b + c == d + e + f == g + h + i and \
           a + d + g == b + e + h == c + f + i and \
           a + e + i == c + e + g


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        nums = 0
        for i in range(0, len(grid) - 2):
            for j in range(0, len(grid[0]) - 2):
                if is_ok(grid[i][j], grid[i][j + 1], grid[i][j + 2],
                         grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                         grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]
                         ):
                    nums += 1
        return nums


if __name__ == '__main__':
    x = [[10, 3, 5], [1, 6, 11], [7, 9, 2]]
    print(Solution().numMagicSquaresInside(x))
