from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        index = 0
        while index < len(nums) and nums[index] != 1:
            index += 1
        last_one = index
        index += 1
        while index < len(nums):
            if nums[index] == 0:
                index += 1
                continue
            else:
                if index - last_one - 1 < k:
                    return False
                last_one = index
                index += 1
        return True


if __name__ == '__main__':
    print(Solution().kLengthApart(nums=[1, 0, 0, 1, 0, 1], k=2))
