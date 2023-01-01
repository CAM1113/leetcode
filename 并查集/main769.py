from typing import List


def find(array, index) -> int:
    if array[index] == index:
        return index
    root = find(array, array[index])
    array[index] = root
    return root


def union(array, index1, index2):
    r1 = find(array, index1)
    r2 = find(array, index2)
    array[r1] = array[r2]


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if (len(arr)) == 1:
            return 1
        arrays = [i for i in range(len(arr))]
        for index, value in enumerate(arr):
            if value == index:
                continue
            if value > index:
                for i in range(index, value + 1):
                    union(arrays, i, index)
            if value < index:
                for i in range(value, index):
                    union(arrays, i, index)
        blocks = set()
        for index in range(len(arrays)):
            root = find(arrays, index)
            blocks.add(root)
        return len(blocks)


def main():
    arr = [1,0,2,3,4]
    print(Solution().maxChunksToSorted(arr))


if __name__ == '__main__':
    main()
