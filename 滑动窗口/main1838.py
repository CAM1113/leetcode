from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        index = len(nums) - 1
        max_len = 0
        used = 0

        while index - max_len >= 0:
            while index - max_len >= 0:
                if nums[index] - nums[index - max_len] + used <= k:
                    used += (nums[index] - nums[index - max_len])
                    max_len += 1
                else:
                    break

            used += nums[index] - nums[index - max_len]
            used -= max_len * (nums[index] - nums[index - 1])
            index -= 1

        return max_len + 1


if __name__ == '__main__':
    print(Solution().maxFrequency([1, 4, 8, 13], k=5))
