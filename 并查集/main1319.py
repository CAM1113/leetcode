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


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        array = [i for i in range(n)]
        if len(connections) < n - 1:
            return -1
        for c in connections:
            root1 = find(array, c[0])
            root2 = find(array, c[1])
            if root1 != root2:
                union(array, root1, root2)

        node_set = set()
        for i in range(len(array)):
            node_set.add(find(array, i))
        return len(node_set) - 1


def main():
    n = 5
    connections = [[0, 1], [0, 2], [3, 4], [2, 3]]
    print(Solution().makeConnected(n, connections=connections))


if __name__ == '__main__':
    main()
