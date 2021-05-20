import heapq
from typing import List


class Heap:
    def __init__(self, length):
        self.length = length
        self.heap = []

    def add(self, x):
        if len(self.heap) < self.length:
            self.heap.append(x)
            if len(self.heap) == self.length:
                self.heap.sort(reverse=False)
            return
        if x < self.heap[0]:
            return
        index = 0
        self.heap[0] = x
        while index < self.length:
            min_index = index
            if index * 2 + 1 < self.length and self.heap[index * 2 + 1] < self.heap[min_index]:
                min_index = index * 2 + 1
            if index * 2 + 2 < self.length and self.heap[index * 2 + 2] < self.heap[min_index]:
                min_index = index * 2 + 2
            if min_index == index:
                break
            temp = self.heap[min_index]
            self.heap[min_index] = self.heap[index]
            self.heap[index] = temp
            index = min_index

    def get_head(self):
        return self.heap[0]


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        xor_matrix = [[0 for _ in matrix[0]] for _ in matrix]
        xor_matrix[0][0] = matrix[0][0]
        heap = []
        heapq.heappush(heap, xor_matrix[0][0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    if j == 0:
                        continue
                    xor_matrix[i][j] = xor_matrix[i][j - 1] ^ matrix[i][j]
                    heapq.heappush(heap, xor_matrix[i][j])
                    continue
                if j == 0:
                    if i == 0:
                        continue
                    xor_matrix[i][j] = xor_matrix[i - 1][j] ^ matrix[i][j]
                    heapq.heappush(heap, xor_matrix[i][j])
                    continue
                # j != 0 and i != 0
                xor_matrix[i][j] = xor_matrix[i - 1][j] ^ xor_matrix[i][j - 1] ^ xor_matrix[i - 1][j - 1] ^ matrix[i][j]
                heapq.heappush(heap, xor_matrix[i][j])

        return heapq.nlargest(k,heap)[-1]


class Solution2:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        xor_matrix = [[0 for _ in matrix[0]] for _ in matrix]
        xor_matrix[0][0] = matrix[0][0]
        heap = Heap(k)
        heap.add(matrix[0][0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    if j == 0:
                        continue
                    xor_matrix[i][j] = xor_matrix[i][j - 1] ^ matrix[i][j]
                    heap.add(xor_matrix[i][j])
                    continue
                if j == 0:
                    if i == 0:
                        continue
                    xor_matrix[i][j] = xor_matrix[i - 1][j] ^ matrix[i][j]
                    heap.add(xor_matrix[i][j])
                    continue
                # j != 0 and i != 0
                xor_matrix[i][j] = xor_matrix[i - 1][j] ^ xor_matrix[i][j - 1] ^ xor_matrix[i - 1][j - 1] ^ matrix[i][j]
                heap.add(xor_matrix[i][j])
        return heap.get_head()


if __name__ == '__main__':
    matrix = [[5, 2], [1, 6]]
    k = 4
    print(Solution().kthLargestValue(matrix, k))
