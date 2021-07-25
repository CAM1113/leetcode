from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda x: x[0])
        index = 1
        while index < len(ranges):
            if ranges[index][0] <= ranges[index - 1][1]+1:
                ranges[index - 1][1] = max(ranges[index - 1][1], ranges[index][1])
                ranges.pop(index)
            else:
                index += 1
        for r in ranges:
            if r[0] <= left and r[1] >= right:
                return True
        return False
