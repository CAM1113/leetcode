from typing import List


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        start = 0
        length = K
        times = 0
        while start + length <= len(A):
            if A[start] == 1:
                start += 1
                continue
            times += 1
            for i in range(start, start + length):
                if A[i] == 0:
                    A[i] = 1
                else:
                    A[i] = 0
            start += 1
        for i in range(start, len(A)):
            if A[i] == 0:
                return -1
        return times


if __name__ == '__main__':
    AA = [0, 1, 0]
    KK = 1
    print(Solution().minKBitFlips(AA, KK))
