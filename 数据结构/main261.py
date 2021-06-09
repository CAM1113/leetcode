from typing import List


def find(array: list, index):
    if array[index] == index:
        return index
    root = find(array, array[index])
    array[index] = root
    return root


def union(array, index1, index2):
    root1 = array[index1]
    root2 = array[index2]
    array[root2] = root1


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        array = [i for i in range(n)]
        for e in edges:
            union(array, e[0], e[1])
        root1 = find(array, 0)
        for idx in range(len(array)):
            if find(array, idx) != root1:
                return False
        return True
