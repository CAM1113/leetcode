from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        cnt_ones = [0] * 30
        for n in nums:
            index = 0
            while n > 0:
                cnt_ones[index] += n & 1
                n >>= 1
                index += 1
        sums = 0
        length = len(nums)
        print(cnt_ones)
        for bit_zero in cnt_ones:
            sums += bit_zero * (length - bit_zero)
        return sums


if __name__ == '__main__':
    x = [4, 14, 2]
    print(Solution().totalHammingDistance(x))
