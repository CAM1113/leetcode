# 给定边，遍历,从图的角度看题
# hash实现
import collections
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        for p in adjacentPairs:
            edges[p[0]].append(p[1])
            edges[p[1]].append(p[0])
        key = 0
        for e in edges.keys():
            if len(edges[e]) == 1:
                key = e
                break
        result = [key]
        key = edges[key][0]
        while True:
            next_nodes = edges[key]
            if len(next_nodes) == 1:
                result.append(key)
                break
            if next_nodes[0] != result[-1]:
                result.append(key)
                key = next_nodes[0]
            else:
                result.append(key)
                key = next_nodes[1]

        return result

if __name__ == '__main__':
    x = [[2,1],[3,4],[3,2]]
    print(Solution().restoreArray(x))