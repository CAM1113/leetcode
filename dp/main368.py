import collections
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        index_dict = collections.defaultdict(list)
        index_dict[0].append(nums[0])
        dp = [1 for _ in nums]
        max_index = 0
        for i in range(1, len(nums)):
            index = i-1
            index_dict[i].append(nums[i])
            while index >= 0:
                if nums[i] % nums[index] == 0 and dp[i] < dp[index] + 1:
                    dp[i] = dp[index] + 1
                    if dp[i] >dp[max_index]:
                        max_index = i
                    index_dict[i] = index_dict[index][:]
                    index_dict[i].append(nums[i])
                index -= 1
        return index_dict[max_index]


if __name__ == '__main__':
    nums = [3,4,6,8,12,16,32]
    print(Solution().largestDivisibleSubset(nums))
