from typing import List, Tuple


class Heap:
    def __init__(self):
        self.heap = []

    def add(self, n: Tuple[int, int, int]):
        self.heap.append(n)
        index = len(self.heap) - 1
        while index > 0:
            father_index = (index-1) // 2
            if self.is_small(self.heap[index], self.heap[father_index]):
                temp = self.heap[father_index]
                self.heap[father_index] = self.heap[index]
                self.heap[index] = temp
                index = father_index
            else:
                break

    def is_small(self, n1, n2):
        if n1[1] < n2[1]:
            return True
        elif n1[1] == n2[1]:
            return n1[2] < n2[2]
        else:
            return False

    def remove(self):
        head = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        index = 0
        while index < len(self.heap):
            if index * 2 + 1 >= len(self.heap):
                break
            min_index = index
            if self.is_small(self.heap[index * 2 + 1], self.heap[index]):
                min_index = index * 2 + 1

            if index * 2 + 2 < len(self.heap) and self.is_small(self.heap[index * 2 + 2], self.heap[min_index]):
                min_index = index * 2 + 2

            if min_index == index:
                break

            temp = self.heap[min_index]
            self.heap[min_index] = self.heap[index]
            self.heap[index] = temp
            index = min_index
        return head

    def length(self):
        return len(self.heap)


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_list = [(t[0], t[1], index) for index, t in enumerate(tasks)]
        task_list.sort(key=lambda x: x[0], reverse=True)
        start_time = 0
        heap = Heap()
        result = []

        while heap.length() != 0 or len(task_list) != 0:

            if heap.length() == 0:
                start_time = task_list[-1][0]
                while len(task_list) > 0:
                    if task_list[-1][0] == start_time:
                        heap.add(task_list[-1])
                        task_list.pop()
                    else:
                        break

            # 执行任务t
            t = heap.remove()
            start_time = start_time + t[1]
            result.append(t[2])

            while len(task_list) > 0:
                if task_list[-1][0] <= start_time:
                    heap.add(task_list[-1])
                    task_list.pop()
                else:
                    break
        return result


if __name__ == '__main__':
    t = [[19, 13], [16, 9], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15], [38, 41], [37, 34], [33, 6], [45, 4],
         [18, 18], [46, 39], [12, 24]]
    print(Solution().getOrder(t))
