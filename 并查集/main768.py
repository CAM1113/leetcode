import collections
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
    array[root1] = root2


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        union_find_array = [i for i in range(len(arr))]
        sorted_array = [i for i in arr]
        sorted_array.sort()
        min_val = 10e9
        max_val = -1
        index_map = collections.defaultdict(lambda: [min_val, max_val])
        for index, value in enumerate(sorted_array):
            index_arr = index_map[value]
            min_index = index_arr[0]
            max_index = index_arr[1]
            if index <= min_index:
                index_arr[0] = index
            if index >= max_index:
                index_arr[1] = index
        for index, value in enumerate(arr):
            min_index = index_map[value][0]
            max_index = index_map[value][1]
            if min_index <= index <= max_index:
                continue
            if min_index > index:
                for i in range(index, min_index + 1):
                    union(union_find_array, i, index)

            if max_index < index:
                for i in range(max_index, index + 1):
                    union(union_find_array, index, i)
        sets = set()
        for index in range(len(arr)):
            root = find(union_find_array, index)
            sets.add(root)
        return len(sets)


def main():
    arr = [1,1,1,0,1,0,0,0,1,0]
    print(Solution().maxChunksToSorted(arr))


if __name__ == '__main__':
    main()
