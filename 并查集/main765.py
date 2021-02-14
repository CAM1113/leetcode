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
    def minSwapsCouples(self, row: List[int]) -> int:
        array = [i for i in range(len(row) // 2)]
        index = 0
        while index < len(row) // 2:
            cp1 = row[2 * index]
            cp2 = row[2 * index + 1]
            union(array, cp1 // 2, cp2 // 2)
            index += 1

        cnt_dic = {}
        for i in range(len(array)):
            root = find(array, i)
            if root in cnt_dic.keys():
                cnt_dic[root] += 1
            else:
                cnt_dic[root] = 1
        sums = 0
        for val in cnt_dic.values():
            sums += val - 1
        return sums


if __name__ == '__main__':
    x = [0, 2, 1, 3]
    print(Solution().minSwapsCouples(x))
