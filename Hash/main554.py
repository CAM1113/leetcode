import collections
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        len_cnt = collections.defaultdict(int)
        for ws in wall:
            sums = 0
            for w in ws:
                sums += w
                len_cnt[sums] += 1
        max_cnt = 0
        del len_cnt[sums]
        for cnt in len_cnt.values():
            if cnt > max_cnt:
                max_cnt = cnt
        return len(wall) - max_cnt

if __name__ == '__main__':
    x = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    print(Solution().leastBricks(x))
