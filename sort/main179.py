# 较大的字符串在前
from typing import List


def compare(s1: str, s2: str):
    shorter = s1
    longer = s2
    if len(s1) > len(s2):
        shorter = s2
        longer = s1
    index = 0
    while index < len(shorter):
        if int(shorter[index]) > int(longer[index]):
            return shorter, longer
        if int(shorter[index]) < int(longer[index]):
            return longer, shorter
        index += 1
    while index < len(longer):
        if int(shorter[index % len(shorter)]) > int(longer[index]):
            return shorter, longer
        if int(shorter[index % len(shorter)]) < int(longer[index]):
            return longer, shorter
        index += 1
    if len(longer) % len(shorter) == 0:
        return shorter, longer

    while True:
        if int(shorter[index % len(shorter)]) > int(longer[index % len(longer)]):
            return shorter, longer
        if int(shorter[index % len(shorter)]) < int(longer[index % len(longer)]):
            return longer, shorter
        index += 1


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return '0'
        nums = [str(i) for i in nums]
        # 冒泡排序
        for i in range(len(nums)):
            for j in range(1, len(nums) - i):
                b, s = compare(nums[j], nums[j - 1])
                nums[j] = s
                nums[j - 1] = b

        return ''.join(nums)
