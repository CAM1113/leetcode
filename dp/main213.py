from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        dp1 = [[0, 0] for _ in range(N - 1)]
        dp2 = [[0, 0] for _ in range(N - 1)]
        dp1[0][0] = nums[0]
        dp2[0][0] = nums[1]
        for i in range(1, N - 1):
            dp1[i][0] = dp1[i - 1][1] + nums[i]
            dp1[i][1] = max(dp1[i - 1][1], dp1[i - 1][0])

            dp2[i][0] = dp2[i - 1][1] + nums[i + 1]
            dp2[i][1] = max(dp2[i - 1][1], dp2[i - 1][0])
        return max(dp1[-1][0], dp1[-1][1], dp2[-1][0], dp2[-1][1])


if __name__ == '__main__':
    x = [2,3,2]
    print(Solution().rob(x))
