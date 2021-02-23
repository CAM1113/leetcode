from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sub_list = []
        index = 0
        start = 0
        max_length = 0
        while index < len(nums):
            sub_list.append(nums[index])
            sub_list.sort()
            if sub_list[-1] - sub_list[0] <= limit:
                index += 1
                if len(sub_list) > max_length:
                    max_length = len(sub_list)
                continue
            while sub_list[-1] - sub_list[0] > limit:
                sub_list.remove(nums[start])
                start += 1
            index += 1
        return max_length


if __name__ == '__main__':
    nums = [8, 2, 4, 7]
    limit = 4
    print(Solution().longestSubarray(nums, limit))
