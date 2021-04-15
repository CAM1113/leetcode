from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while start < end - 1:
            middle = (start + end) // 2
            if nums[middle] == target:
                return True
            if nums[start] == nums[middle]:
                start += 1
                continue
            if nums[start] < nums[middle]:
                if target < nums[start]:
                    start = middle
                    continue
                if target == nums[start]:
                    return True
                if nums[start] < target < nums[middle]:
                    end = middle
                    continue
                if target > nums[middle]:
                    start = middle
                    continue
            if nums[start] > nums[middle]:
                if target < nums[middle]:
                    end = middle
                    continue
                if nums[middle] < target < nums[end]:
                    start = middle
                    continue
                if target == nums[end]:
                    return True
                if target > nums[end]:
                    end = middle
                    continue
        return nums[start] == target or nums[end] == target


if __name__ == '__main__':
    nums = [1, 0, 1, 1, 1]
    target = 2
    print(Solution().search(nums, target))
