from typing import List


def find(array, index):
    if array[index] == index:
        return index
    root = find(array, array[index])
    array[index] = root
    return root


def union(array, index1, index2):
    root1 = find(array, index1)
    root2 = find(array, index2)
    array[root2] = root1


class Edge:
    def __init__(self, x, y, l):
        self.x = x
        self.y = y
        self.l = l


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        array = [i for i in range(len(heights) * len(heights[0]))]
        edges = []
        m = len(heights)
        n = len(heights[0])
        for i in range(m):
            for j in range(n):
                if j + 1 < n:
                    edges.append(Edge(i * n + j, i * n + j + 1, abs(heights[i][j + 1] - heights[i][j])))
                if i + 1 < m:
                    edges.append(Edge(i * n + j, (i + 1) * n + j, abs(heights[i + 1][j] - heights[i][j])))
        edges.sort(key=lambda x: x.l)
        for e in edges:
            if find(array, e.x) != find(array, e.y):
                union(array, e.x, e.y)
                if find(array, 0) == find(array, m * n - 1):
                    return e.l


if __name__ == '__main__':
    x = [[1,2,3],[3,8,4],[5,3,5]]
    print(Solution().minimumEffortPath(x))
