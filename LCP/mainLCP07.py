import collections
from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        level = [0]
        step = 0
        path = collections.defaultdict(list)
        for r in relation:
            path[r[0]].append(r[1])

        while len(level) != 0 and step < k:
            step += 1
            next_level = []
            for x in level:
                next_level += list(path[x])
            level = next_level
        cnt = 0
        for x in level:
            if x == n-1:
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().numWays(n=5, relation=[[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]], k=3))
