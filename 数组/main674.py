from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        start = 0
        point = 0
        max_length = 1
        while point < len(nums) - 1:
            if nums[point] >= nums[point + 1]:
                if point - start + 1 > max_length:
                    max_length = point - start + 1
                start = point + 1
            point += 1

        if point - start+1 > max_length:
            max_length = point - start +1
        return max_length


if __name__ == '__main__':
    x = [1,3,5,4,2,3,4,5]
    print(Solution().findLengthOfLCIS(x))
