from typing import List


def adjust(heap, index):
    if index == 0:
        return
    father = (index - 1) // 2
    if heap[father] > heap[index]:
        te = heap[father]
        heap[father] = heap[index]
        heap[index] = te
        adjust(heap, father)


def build_heap(heap: List):
    for i in range(1, len(heap)):
        adjust(heap, i)


def add_head(heap: List, index):
    if index * 2 + 2 < len(heap):
        if heap[index * 2 + 1] <= heap[index * 2 + 2]:
            min_index = index * 2 + 1
        else:
            min_index = index * 2 + 2
        if heap[min_index] < heap[index]:
            temp = heap[index]
            heap[index] = heap[min_index]
            heap[min_index] = temp
            add_head(heap, min_index)

    elif index * 2 + 1 < len(heap) and heap[index * 2 + 1] < heap[index]:
        temp = heap[index]
        heap[index] = heap[index * 2 + 1]
        heap[index * 2 + 1] = temp
        add_head(heap, index * 2 + 1)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        build_heap(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                add_head(heap, 0)
        return heap[0]


if __name__ == '__main__':
    s = [5, 2, 4, 1, 3, 6, 0]
    kk = 4
    print(Solution().findKthLargest(s, kk))
