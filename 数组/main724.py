from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return -1
        sum_arr = [0]
        for i in range(len(nums)):
            sum_arr.append(sum_arr[-1] + nums[i])
        for i in range(1, len(sum_arr)):
            if sum_arr[i - 1] == sum_arr[-1] - sum_arr[i]:
                return i - 1
        return -1


if __name__ == '__main__':
    n = [1, 7, 3, 6, 5, 6]
    print(Solution().pivotIndex(n))
