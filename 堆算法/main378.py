from typing import List


class MaxHeap:
    def __init__(self, k):
        self.heap = [10 ** 9] * k

    def adjust(self, index):
        if 2 * index + 1 >= len(self.heap):
            return
        max_index = index * 2 + 1
        if index * 2 + 2 < len(self.heap):
            if self.heap[index * 2 + 2] > self.heap[index * 2 + 1]:
                max_index = index * 2 + 2
        if self.heap[max_index] > self.heap[index]:
            val = self.heap[index]
            self.heap[index] = self.heap[max_index]
            self.heap[max_index] = val
        self.adjust(max_index)

    def head(self):
        return self.heap[0]

    def head_val(self, x):
        self.heap[0] = x
        self.adjust(0)


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = MaxHeap(k)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i * j > k:
                    continue
                if matrix[i][j] < heap.head():

                    heap.head_val(matrix[i][j])

        return heap.head()
