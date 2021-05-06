from typing import List


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        start = 0
        end = len(nums)-1
        while start + 1 <= end:
            if nums[start] + nums[end] == target:
                result.append([nums[start],nums[end]])
                start += 1
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return result
