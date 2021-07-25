from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max_left = nums[0]
        min_right = nums[1]
        min_right_index = 1
        for i in range(1, len(nums)):
            if nums[i] <= min_right:
                min_right = nums[i]
                min_right_index = i

        left_index = 0
        while max_left > min_right:
            for i in range(left_index, min_right_index + 1):
                if nums[i] > max_left:
                    max_left = nums[i]

            start = min_right_index + 1
            min_right = nums[-1]
            min_right_index = len(nums) - 1
            for i in range(start, len(nums)):
                if nums[i] < min_right:
                    min_right = nums[i]
                    min_right_index = i
            left_index = start
        return left_index


if __name__ == '__main__':
    print(Solution().partitionDisjoint([1, 1, 1, 0, 6, 12]))
