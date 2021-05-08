class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        sums = 0
        for i in range(n):
            sums ^= (start + i * 2)
        return sums
