from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 1:
            return True
        index = 0
        temp = A[-1] > A[0]

        while index + 1 < len(A):
            if (A[index + 1] > A[index]) != temp:
                return False
        return True
