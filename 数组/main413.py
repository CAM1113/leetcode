from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        len_lis = []
        start = 0
        end = 1
        minus = nums[end] - nums[start]
        while start < len(nums) and end < len(nums):
            if nums[end] - nums[end - 1] == minus:
                end += 1
            else:
                len_lis.append(end - start)
                start = end - 1
                minus = nums[end] - nums[start]
        len_lis.append(end - start)
        result = 0
        for l in len_lis:
            if l < 3:
                continue
            else:
                result += (l - 1) * (l - 2) // 2

        return result


if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices(nums=[1, 2, 3, 4, 3, 2, 1, 2]))
