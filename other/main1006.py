class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N == 3:
            return 6
        sums = N * (N - 1) // (N - 2) + (N - 3)
        N -= 4

        while N > 4:
            sums = sums - N * (N - 1) // (N - 2) + (N - 3)
            N -= 4
        if N > 0:
            n1 = N
            n2 = max(1, N - 1)
            n3 = max(1, N - 2)
            n4 = max(0, N - 3)
            sums = sums - n1 * n2 // n3 + n4

        return sums


if __name__ == '__main__':
    x = 10
    print(Solution().clumsy(x))
