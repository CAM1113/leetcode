from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        min_index = 0
        index = 0
        while index < len(nums):
            if min_index >= len(nums) - 1:
                return True
            if min_index >= index:
                max_index = nums[index] + index
                if max_index > min_index:
                    min_index = max_index
            else:
                break
            index += 1
        return min_index >= len(nums) - 1


if __name__ == '__main__':
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))
