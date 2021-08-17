import collections
from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        importance_dic = collections.defaultdict(lambda: {})
        for index, p in enumerate(preferences):
            for index2, v in enumerate(p):
                importance_dic[index][v] = index2
        result = set()
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                x, y = pairs[i][0], pairs[i][1]
                u, v = pairs[j][0], pairs[j][1]
                if importance_dic[x][u] < importance_dic[x][y] and \
                        importance_dic[u][x] < importance_dic[u][v]:
                    result.add(x)
                    result.add(u)

                if importance_dic[x][v] < importance_dic[x][y] and \
                        importance_dic[v][x] < importance_dic[v][u]:
                    result.add(x)
                    result.add(v)

                if importance_dic[y][u] < importance_dic[y][x] and \
                        importance_dic[u][y] < importance_dic[u][v]:
                    result.add(y)
                    result.add(u)

                if importance_dic[y][v] < importance_dic[y][x] and \
                        importance_dic[v][y] < importance_dic[v][u]:
                    result.add(y)
                    result.add(v)

        return len(result)


if __name__ == '__main__':
    print(Solution().unhappyFriends(n=4, preferences=[[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]],
                                    pairs=[[0, 1], [2, 3]]))
