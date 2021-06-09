from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        start = lower - 1
        result = []
        for index in range(len(nums)):
            result.append((start + 1, nums[index] - 1))
            start = nums[index]
        result.append((start + 1, upper))
        str_result = []
        for r in result:
            if r[1] < r[0]:
                continue
            if r[1] == r[0]:
                str_result.append(f"{r[0]}")
            else:
                str_result.append(f"{r[0]}->{r[1]}")
        return str_result


if __name__ == '__main__':
    s = [0, 1, 3, 50, 75]
    l = 0
    u = 99
    print(Solution().findMissingRanges(s, l, u))
