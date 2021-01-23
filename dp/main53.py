# 给定一个整数数组 nums ，
# 找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

from typing import List

import sys


class Solut ion:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [[i for i in nums] for _ in range(len(nums))]
        min_sum = max(nums)
        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                sums[i][j] = sums[i - 1][j] + sums[0][j - i]
                if sums[i][j] > min_sum:
                    min_sum = sums[i][j]
        return min_sum


if __name__ == '__main__':
    ns = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(ns))  # 6
