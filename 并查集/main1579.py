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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: x[0], reverse=True)
        a_array = [i for i in range(n)]
        b_array = a_array[:]
        is_used = [0 for _ in edges]
        for index, e in enumerate(edges):
            if e[0] == 3:
                root1 = find(a_array, e[1] - 1)
                root2 = find(a_array, e[2] - 1)
                if root1 != root2:
                    union(a_array, root1, root2)
                    union(b_array, root1, root2)
                    is_used[index] = 1
            elif e[0] == 2:
                # 只能b通过
                root1 = find(b_array, e[1] - 1)
                root2 = find(b_array, e[2] - 1)
                if root1 != root2:
                    union(b_array, root1, root2)
                    is_used[index] = 1
            elif e[0] == 1:
                # 只能a通过
                root1 = find(a_array, e[1] - 1)
                root2 = find(a_array, e[2] - 1)
                if root1 != root2:
                    union(a_array, root1, root2)
                    is_used[index] = 1
        a = find(a_array, 0)
        b = find(b_array, 0)
        for i in range(n):
            if find(a_array, i) != a or find(b_array, i) != b:
                return -1
        return len(edges) - sum(is_used)


def main():
    n = 4
    edges = [[3, 1, 2], [3, 3, 4], [1, 1, 3], [2, 2, 4]]
    print(Solution().maxNumEdgesToRemove(n, edges))


if __name__ == '__main__':
    main()
