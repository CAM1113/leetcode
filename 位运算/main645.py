from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n_t_bit = 0
        n_bit = 0
        repeat = set()
        p = 0
        for i in range(1, len(nums) + 1):
            n_t_bit ^= i
            n_bit ^= nums[i - 1]
            if p == 0:
                if nums[i - 1] in repeat:
                    p = nums[i - 1]
                else:
                    repeat.add(nums[i - 1])

        return [p,n_t_bit ^ n_bit ^ p]
