from typing import List


def adjust(heap: List[int], index: int):
    if index * 2 + 1 >= len(heap):
        return
    max_index = index * 2 + 1
    if index * 2 + 2 < len(heap) and heap[index * 2 + 2] > heap[index * 2 + 1]:
        max_index = index * 2 + 2
    if heap[max_index] > heap[index]:
        temp = heap[max_index]
        heap[max_index] = heap[index]
        heap[index] = temp
        adjust(heap, max_index)


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr):
            return arr
        if k <= 0:
            return []
        heap = arr[:k]
        heap.sort(reverse=True)
        for i in range(k, len(arr)):
            if arr[i] < heap[0]:
                heap[0] = arr[i]
                adjust(heap, 0)
        return heap


if __name__ == '__main__':
    a = [3, 2, 1]
    k = 2
    print(Solution().getLeastNumbers(a, k))
