class Solution:
    def hammingWeight(self, n: int) -> int:
        cnts = 0
        for i in range(32):
            if n == 0:
                return cnts
            if n % 2 == 1:
                cnts += 1
            n //= 2
        return cnts

if __name__ == '__main__':
    c = 0b11111111111111111111111111111101
    print(Solution().hammingWeight(c))