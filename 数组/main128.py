from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        start = 0
        index = 1
        max_len = 1
        while index < len(nums):
            if nums[index] == nums[index - 1]+1:
                index += 1
            else:
                if index - start > max_len:
                    max_len = index - start
                start = index
                index += 1
        if index - start > max_len:
            max_len = index - start
        return max_len


if __name__ == '__main__':
    n = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    print(Solution().longestConsecutive(n))
