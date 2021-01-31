from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start < end - 1:
            middle = (start + end) // 2
            if nums[middle] < nums[end]:
                end = middle
            else:
                start = middle
        return min(nums[start],nums[end])


if __name__ == '__main__':
    nums = [11,13,15,17]
    print(Solution().findMin(nums))
