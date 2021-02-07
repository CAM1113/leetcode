from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        start = 0
        error_count = 0
        while start + 1 < len(nums):
            if nums[start] <= nums[start + 1]:
                start += 1
            else:
                if error_count == 1:
                    return False
                error_count = 1
                if start == 0 or nums[start + 1] >= nums[start - 1]:
                    start += 1
                    continue
                else:
                    nums[start+1] = nums[start]
                    start += 1
        return True


if __name__ == '__main__':
    nums = [3, 4, 2, 3]
    print(Solution().checkPossibility(nums))
