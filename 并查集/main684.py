from typing import List


# 拓扑排序方法
class Solution1:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mask = 1
        set_mask = [0] * (len(edges) + 1)
        for e in edges:
            if set_mask[e[0]] != 0 and set_mask[e[1]] != 0:
                if set_mask[e[0]] == set_mask[e[1]]:
                    return e
                v1 = set_mask[e[0]]
                v2 = set_mask[e[1]]
                for index in range(len(set_mask)):
                    if set_mask[index] == v1:
                        set_mask[index] = v2
            if set_mask[e[0]] == 0 and set_mask[e[1]] == 0:
                set_mask[e[0]] = mask
                set_mask[e[1]] = mask
                mask += 1
            if set_mask[e[0]] != 0 and set_mask[e[1]] == 0:
                set_mask[e[1]] = set_mask[e[0]]

            if set_mask[e[0]] == 0 and set_mask[e[1]] != 0:
                set_mask[e[0]] = set_mask[e[1]]


# 并查集方法
class Solution:

    def find(self, array, index1):
        if array[index1] == index1:
            return index1
        return self.find(array, array[index1])

    def union(self, array, index1, index2):
        root1 = self.find(array, index1)
        root2 = self.find(array, index2)
        if root1 == root2:
            return False
        array[root2] = root1
        return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        array = [i for i in range(len(edges) + 1)]
        for e in edges:
            root1 = self.find(array,e[0])
            root2 = self.find(array,e[1])
            if root1 == root2:
                return e
            else:
                self.union(array,root1,root2)



if __name__ == '__main__':
    arr = [[1, 2], [1, 3], [2, 3]]
    print(Solution().findRedundantConnection(arr))
