from heapq import nlargest
from typing import List


def up_adjust(arr, index):
    if index == 0:
        return
    father = (index - 1) // 2
    if arr[father] >= arr[index]:
        return
    temp = arr[father]
    arr[father] = arr[index]
    arr[index] = temp
    up_adjust(arr, father)


def down_adjust(arr, index):
    left = index * 2 + 1
    right = index * 2 + 2
    max_index = index
    if left < len(arr) and arr[left] > arr[max_index]:
        max_index = left
    if right < len(arr) and arr[right] > arr[max_index]:
        max_index = right
    if max_index == index:
        return
    temp = arr[max_index]
    arr[max_index] = arr[index]
    arr[index] = temp
    down_adjust(arr, max_index)


class Heap:
    def __init__(self):
        self.heap = []

    def add(self, val):
        self.heap.append(val)
        up_adjust(self.heap, len(self.heap) - 1)

    def pop(self):
        val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        down_adjust(self.heap, 0)
        return val

    def is_empty(self):
        return len(self.heap) <= 0


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(nlargest(k, profits))
        heap = Heap()
        while k > 0:
            index = 0
            while index < len(capital):
                c = capital[index]
                if c <= w:
                    heap.add(profits[index])
                    profits.pop(index)
                    capital.pop(index)
                    continue
                index += 1
            if heap.is_empty():
                return w
            val = heap.pop()
            w += val
            k -= 1
        return w