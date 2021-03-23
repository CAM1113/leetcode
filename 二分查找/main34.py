from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        index = -1
        if nums[start] == target:
            index = start

        elif nums[end] == target:
            index = end
        else:
            while start < end - 1:
                middle = (start + end) // 2
                if nums[middle] == target:
                    index = middle
                    break
                if nums[middle] < target:
                    start = middle
                else:
                    end = middle

        if index == -1:
            return [index, index]
        sub = 0
        while index - sub >= 0:
            if nums[index - sub] == target:
                sub += 1
            else:
                break
        sub -= 1
        add = 0
        while index + add < len(nums):
            if nums[index + add] == target:
                add += 1
            else:
                break
        add -= 1
        return [index - sub, index + add]


if __name__ == '__main__':
    n = [5, 7, 7, 8, 8, 10]
    t = 8
    print(Solution().searchRange(n, t))
