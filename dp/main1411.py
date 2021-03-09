class Solution:
    def numOfWays(self, n: int) -> int:
        aba = [6] * n
        abc = [6] * n
        for i in range(1, n):
            aba[i] = aba[i - 1] * 3 + abc[i - 1] * 2
            abc[i] = aba[i - 1] * 2 + abc[i - 1] * 2
        return int((aba[n - 1] + abc[n - 1]) % (1e9 + 7))

if __name__ == '__main__':
    x = 7
    print(Solution().numOfWays(x))
