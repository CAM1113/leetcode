from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        max_avg = sums / k
        start = 1
        while start + k - 1 < len(nums):
            sums = sums - nums[start - 1] + nums[start + k - 1]
            avg = sums / k
            if avg > max_avg:
                max_avg = avg
            start += 1
        return max_avg


if __name__ == '__main__':
    s = [1, 12, -5, -6, 50, 3]
    k = 4
    print(Solution().findMaxAverage(s, k))
