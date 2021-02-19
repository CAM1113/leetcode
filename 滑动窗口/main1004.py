from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0
        length = 0
        total_zero = 0
        while start + length < len(A):
            if A[start + length] == 1:
                length += 1
                continue
            total_zero += 1
            if total_zero <= K:
                length += 1
                continue
            while total_zero > K:
                if A[start] == 0:
                    total_zero -= 1
                start += 1
                if start + length == len(A):
                    break
                if A[start + length] == 0:
                    total_zero += 1
        return length


if __name__ == '__main__':
    AA = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    KK = 2
    print(Solution().longestOnes(AA, KK))
