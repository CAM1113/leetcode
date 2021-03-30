class Solution:
    def reverseBits(self, n: int) -> int:
        re = 0
        for i in range(31):
            if n & 1 == 1:
                re = re | 1
            n = n >> 1
            re = re << 1
        if n & 1 == 1:
            re = re | 1
        return re


if __name__ == '__main__':
    n = 0b11111111111111111111111111111101
    print(Solution().reverseBits(n))
