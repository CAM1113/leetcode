import collections


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        level = collections.defaultdict(lambda: 0)
        level[(startRow, startColumn)] = 1
        result = 0
        mod = 10 ** 9 + 7
        current_move = 0
        while len(level) > 0 and current_move < maxMove:
            current_move += 1
            next_level = collections.defaultdict(lambda: 0)
            for k in level.keys():
                r, c = k[0], k[1]
                if r - 1 < 0:
                    result += level[k]
                else:
                    next_level[(r - 1, c)] += level[k]
                if r + 1 >= m:
                    result += level[k]
                else:
                    next_level[(r + 1, c)] += level[k]
                if c - 1 < 0:
                    result += level[k]
                else:
                    next_level[(r, c - 1)] += level[k]
                if c + 1 >= n:
                    result += level[k]
                else:
                    next_level[(r, c + 1)] += level[k]
            level = next_level
        return result % mod


if __name__ == '__main__':
    print(Solution().findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
