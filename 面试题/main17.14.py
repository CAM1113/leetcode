# 堆算法
from typing import List


def adjust_heap(arr: List[int]):
    index = 0
    while index * 2 + 1 < len(arr):
        min_index = index
        if arr[index * 2 + 1] > arr[index]:
            min_index = index * 2 + 1
        if index * 2 + 2 < len(arr) and arr[index * 2 + 2] > arr[min_index]:
            min_index = index * 2 + 2
        if min_index == index:
            break
        temp = arr[index]
        arr[index] = arr[min_index]
        arr[min_index] = temp
        index = min_index


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        heap = arr[:k]
        heap.sort(reverse=True)
        for i in range(k, len(arr)):
            if arr[i] < heap[0]:
                heap[0] = arr[i]
                adjust_heap(heap)
        return heap


if __name__ == '__main__':
    x = [1, 3, 5, 7, 2, 4, 6, 8]
    kk = 4
    print(Solution().smallestK(x, kk))
