from typing import List


# O(n**2)的时间复杂度
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        index = 1
        while index < len(nums):
            if nums[index - 1] == nums[index]:
                nums.pop(index)
            else:
                index += 1

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0:
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                j -= 1
        return dp[-1]


# O(n*log(n))的时间复杂度

class Solution:
    @staticmethod
    def binary_search(array: List, val):
        start = 0
        end = len(array) - 1
        while start < end - 1:
            middle = (start + end) // 2
            if array[middle] < val:
                start = middle
            else:
                end = middle
        if array[start] > val:
            return start
        return end

    def lengthOfLIS(self, nums: List[int]) -> int:
        index = 1
        while index < len(nums):
            if nums[index - 1] == nums[index]:
                nums.pop(index)
            else:
                index += 1
        le = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > le[-1]:
                le.append(nums[i])
            else:
                p = self.binary_search(le, nums[i])
                if p - 1 >= 0 and le[p - 1] == nums[i]:
                    continue
                le[p] = nums[i]
        return len(le)


if __name__ == '__main__':
    x =   [7,7,7,7,7,7,7]
    print(Solution().lengthOfLIS(x))
