from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end - 1:
            middle = (start + end) // 2
            if nums[middle] == nums[end]:
                while end - 1 > start and nums[end] == nums[middle]:
                    end -= 1
                if end < middle:
                    end += 1
                continue
            if nums[middle] < nums[end]:
                end = middle
                continue
            if nums[middle] > nums[end]:
                start = middle
                continue
        return min(nums[start], nums[end])

if __name__ == '__main__':
    x = [2, 2, 0, 0, 0]
    print(Solution().findMin(x))
