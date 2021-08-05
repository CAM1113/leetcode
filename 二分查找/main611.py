from typing import List


def binary_search(nums, start, sums):
    end = len(nums) - 1

    if sums <= nums[start]:
        return start - 1
    if sums > nums[-1]:
        return len(nums) - 1

    while start < end - 1:
        middle = (start + end) // 2
        if sums > nums[middle]:
            start = middle
        else:
            end = middle
    return start


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        results = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                sums = nums[i] + nums[j]

                index = binary_search(nums, j + 1, sums)
                results += index - j
        return results


if __name__ == '__main__':
    print(Solution().triangleNumber([2, 2, 3, 4]))
