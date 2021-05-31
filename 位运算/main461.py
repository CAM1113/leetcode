class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        length = 0
        while z > 0:
            if z & 1 == 1:
                length += 1
                z = z >> 1
        return length
