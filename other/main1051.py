from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = heights[:]
        target.sort()
        num = 0
        for i in range(len(heights)):
            if heights[i] != target[i]:
                num += 1
        return num - 1
