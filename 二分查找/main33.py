from typing import List


def find_index(nums, target, start, end):
    while start < end - 1:
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            start = middle
        else:
            end = middle
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        start = 0
        end = len(nums) - 1
        while start < end - 1:
            middle = (start + end) // 2
            if nums[middle] > nums[start]:
                start = middle
            else:
                end = middle
        if nums[0] <= target <= nums[start]:
            return find_index(nums, target, 0, start)
        else:
            return find_index(nums, target, end, len(nums) - 1)


if __name__ == '__main__':
    n = [4, 5, 6, 7, 0, 1, 2]
    t = 0
    print(Solution().search(n, t))
