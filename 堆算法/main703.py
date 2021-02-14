from typing import List


def adjust(array: List, index):
    if index * 2 + 1 >= len(array):
        return
    min_index = index * 2 + 1
    if index * 2 + 2 < len(array) and array[index * 2 + 2] < array[index * 2 + 1]:
        min_index = index * 2 + 2
    if array[min_index] < array[index]:
        temp = array[min_index]
        array[min_index] = array[index]
        array[index] = temp
        adjust(array, min_index)


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if k == 1:
            if len(nums) == 0:
                self.max_val = -10000
            else:
                self.max_val = max(nums)
        nums.sort(reverse=True)
        nums = nums[:k]
        self.nums = nums[::-1]
        self.k = k

    def add(self, val: int) -> int:
        if self.k == 1:
            if val > self.max_val:
                self.max_val = val
            return self.max_val

        if self.k > len(self.nums):
            self.nums.append(val)
            self.nums.sort()
            return self.nums[0]

        if val > self.nums[0]:
            self.nums[0] = val
            adjust(self.nums, 0)
        return self.nums[0]


if __name__ == '__main__':
    x = KthLargest(2, [0])
    x.add(-1)
    x.add(1)
    x.add(-2)
    x.add(-4)
    x.add(3)
