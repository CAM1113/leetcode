from typing import List


class Solution2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        last = 0
        current = 1
        while current < len(arr):
            if arr[current] < arr[last]:
                return last
            current += 1
            last += 1


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        while start < end - 1:
            middle = (start + end) // 2
            if arr[middle - 1] < arr[middle] < arr[middle + 1]:
                start = middle
                continue
            if arr[middle - 1] > arr[middle] > arr[middle + 1]:
                end = middle
                continue
            if arr[middle - 1] < arr[middle] and arr[middle + 1] < arr[middle]:
                return middle
