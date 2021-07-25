import sys
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        abses = []
        mod = 10 ** 9 + 7
        for i in range(len(nums1)):
            abses.append((abs(nums1[i] - nums2[i]), i))
        abses.sort(reverse=True, key=lambda x: x[0])
        current_reduce = 0
        for i in range(len(abses)):
            gap = abses[i][0]
            if gap < current_reduce:
                break
            for j in range(len(nums1)):
                if gap - abs(nums1[j] - nums2[abses[i][1]]) > current_reduce:
                    current_reduce = gap - abs(nums1[j] - nums2[abses[i][1]])
        sums = 0
        for v in abses:
            sums += v[0]
            sums %= mod
        sums -= current_reduce
        return sums % mod


if __name__ == '__main__':
    print(Solution().minAbsoluteSumDiff(
        nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
    ))
