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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        array = [i for i in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1:
                    union(array, i, j)
        num_set = set()
        for i in range(len(array)):
            num_set.add(find(array, i))
        return len(num_set)
