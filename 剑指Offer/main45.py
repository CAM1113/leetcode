import functools
from typing import List


def is_bigger(str1: str, str2: str):
    index = 0
    max_len = max(len(str1), len(str2)) * 2
    while index < max_len:
        if str1[index % len(str1)] < str2[index % len(str2)]:
            return -1
        elif str1[index % len(str1)] > str2[index % len(str2)]:
            return 1
        index += 1
    return 0


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        re = [str(n) for n in nums]
        re = sorted(re, key=functools.cmp_to_key(is_bigger))
        return ''.join(re)


if __name__ == '__main__':
    x = [3, 30, 34, 5, 9]
    print(Solution().minNumber(x))
    print(is_bigger('3', '30'))
