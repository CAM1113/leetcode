import collections
import heapq
from typing import List


class Heap:
    def __init__(self, k):
        self.heap = []
        self.k = k

    def push(self, val):
        if len(self.heap) < self.k:
            self.heap.append(val)
            if len(self.heap) == self.k:
                self.heap.sort(key =lambda x:x[1])
            return
        if val[1] > self.heap[0][1]:
            self.heap[0] = val
            self.adjust(0)

    def adjust(self, index):
        if index * 2 + 1 >= self.k:
            return
        min_index = index
        left = index * 2 + 1
        right = index * 2 + 2
        if left < self.k and self.heap[left][1] < self.heap[min_index][1]:
            min_index = left
        if right < self.k and self.heap[right][1] < self.heap[min_index][1]:
            min_index = right
        if min_index == index:
            return
        else:
            temp = self.heap[min_index]
            self.heap[min_index] = self.heap[index]
            self.heap[index] = temp
            self.adjust(min_index)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.defaultdict(lambda: 0)
        h = Heap(k)
        for n in nums:
            cnt[n] += 1
        for k, v in cnt.items():
            h.push((k, v))
        return [k for (k, v) in h.heap]


if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[5,2,5,3,5,3,1,1,3], k=2))
