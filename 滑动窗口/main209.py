from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        length = 0
        sums = 0
        min_length = 1e10
        while start + length < len(nums):
            if sums + nums[start + length] < s:
                sums += nums[start + length]
                length += 1
                continue
            if length < min_length:
                min_length = length
            sums -= nums[start]
            start += 1
            length -= 1
        return min_length + 1


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(s, nums))
