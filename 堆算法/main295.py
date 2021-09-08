def adjust_down(heap, index, is_small):
    left = index * 2 + 1
    right = index * 2 + 2
    min_index = index
    if left < len(heap):
        if is_small and heap[min_index] > heap[left]:
            min_index = left
        if not is_small and heap[min_index] < heap[left]:
            min_index = left
    if right < len(heap):
        if is_small and heap[min_index] > heap[right]:
            min_index = right
        if not is_small and heap[min_index] < heap[right]:
            min_index = right
    if min_index == index:
        return
    t = heap[index]
    heap[index] = heap[min_index]
    heap[min_index] = t
    adjust_down(heap, min_index, is_small)


def adjust_up(heap, index, is_small):
    if index == 0:
        return
    father = (index - 1) // 2
    if is_small and heap[father] > heap[index]:
        t = heap[father]
        heap[father] = heap[index]
        heap[index] = t
        adjust_up(heap, father, is_small)

    if not is_small and heap[father] < heap[index]:
        t = heap[father]
        heap[father] = heap[index]
        heap[index] = t
        adjust_up(heap, father, is_small)


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.len = 0
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if len(self.left_heap) == len(self.right_heap):
            if len(self.left_heap) == 0:
                self.left_heap.append(num)
                return
            insert_val = num
            if len(self.right_heap) > 0 and self.right_heap[0] < num:
                insert_val = self.right_heap[0]
                self.right_heap[0] = num
                adjust_down(self.right_heap, 0, True)
            self.left_heap.append(insert_val)
            adjust_up(self.left_heap, len(self.left_heap) - 1, False)
            return

        if len(self.left_heap) == len(self.right_heap) + 1:
            insert_val = num
            if self.left_heap[0] > num:
                insert_val = self.left_heap[0]
                self.left_heap[0] = num
                adjust_down(self.left_heap, 0, False)
            self.right_heap.append(insert_val)
            adjust_up(self.right_heap, len(self.right_heap) - 1, True)
            return

    def findMedian(self) -> float:
        if (len(self.left_heap) + len(self.right_heap)) % 2 == 0:
            return (self.left_heap[0] + self.right_heap[0]) / 2.0
        return self.left_heap[0]

