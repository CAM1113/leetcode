from copy import deepcopy
from typing import List


def get_val(s):
    bit = 0
    ha = 0
    for lis in s:
        for val in lis:
            bit += 1
            ha += val * (10 ** bit)
    return ha


def get_start(board: List[List[int]]):
    row = -1
    for lis in board:
        col = -1
        row += 1
        for val in lis:
            col += 1
            if val == 0:
                return row, col
    raise Exception("beyond bound,no start")


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = get_start(board)
        level = [(board, start)]
        used = set()
        step = -1
        target = get_val([[1, 2, 3], [4, 5, 0]])
        while len(level) != 0:
            step += 1
            next_level = []
            for (b, s) in level:
                hash_val = get_val(b)
                if hash_val in used:
                    continue
                used.add(hash_val)

                if hash_val == target:
                    return step
                row, col = s
                if row - 1 >= 0:
                    tb = deepcopy(b)
                    tv = tb[row][col]
                    tb[row][col] = tb[row - 1][col]
                    tb[row - 1][col] = tv
                    if get_val(tb) not in used:
                        next_level.append((tb, (row - 1, col)))
                if row + 1 <= 1:
                    tb = deepcopy(b)
                    tv = tb[row][col]
                    tb[row][col] = tb[row + 1][col]
                    tb[row + 1][col] = tv
                    if get_val(tb) not in used:
                        next_level.append((tb, (row + 1, col)))

                if col - 1 >= 0:
                    tb = deepcopy(b)
                    tv = tb[row][col]
                    tb[row][col] = tb[row][col - 1]
                    tb[row][col - 1] = tv
                    if get_val(tb) not in used:
                        next_level.append((tb, (row, col - 1)))

                if col + 1 <= 2:
                    tb = deepcopy(b)
                    tv = tb[row][col]
                    tb[row][col] = tb[row][col + 1]
                    tb[row][col + 1] = tv
                    if get_val(tb) not in used:
                        next_level.append((tb, (row, col + 1)))
            level = next_level
        return -1


if __name__ == '__main__':
    b = [[1, 2, 3], [5, 4, 0]]
    print(Solution().slidingPuzzle(b))
