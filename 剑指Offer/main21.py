from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] % 2 == 0:
                while start < end and nums[end] % 2 == 0:
                    end -= 1
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
            start += 1
        return nums


if __name__ == '__main__':
    nums = [1]
    print(Solution().exchange(nums))
