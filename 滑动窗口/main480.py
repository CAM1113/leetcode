from typing import List


def remove(array: List[int], x: int):
    start = 0
    end = len(array) - 1
    while start < end - 1:
        middle = (start + end) // 2
        if array[middle] < x:
            start = middle
        else:
            end = middle
    if array[start] == x:
        array.pop(start)
        return
    if array[end] == x:
        array.pop(end)
        return


def insert(array: list, x):
    start = 0
    end = len(array) - 1
    while start < end - 1:
        middle = (start + end) // 2
        if array[middle] < x:
            start = middle
        else:
            end = middle
    if len(array) == 0:
        array.append(x)
        return
    if array[start] > x:
        array.insert(start, x)
    elif array[start] <= x <= array[end]:
        array.insert(start + 1, x)
    elif array[end] < x:
        array.insert(end + 1, x)


def find_middle(array: List[int]):
    if len(array) % 2 == 0:
        i = (len(array) - 1) // 2
        return (array[i] + array[i + 1]) / 2.0
    else:
        i = len(array) // 2
        return array[i]


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        sub_list = nums[:k]
        sub_list.sort()
        start = 0
        result = []
        while start + k < len(nums):
            result.append(find_middle(sub_list))
            remove(sub_list, nums[start])
            insert(sub_list, nums[start + k])
            start += 1
        result.append(find_middle(sub_list))
        return result


if __name__ == '__main__':
    n = [7,9,3,8,0,2,4,8,3,9]
    k = 1
    print(Solution().medianSlidingWindow(n, k))
