class Solution:
    def numWays(self, n: int) -> int:
        nums = [1 for _ in range(n + 1)]
        for i in range(2, len(nums)):
            nums[i] = nums[i - 1] + nums[i - 2]
        return nums[-1]%1000000007