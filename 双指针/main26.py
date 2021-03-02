from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        start = 0
        end = 1
        temp = nums[start]
        while end < len(nums):
            if nums[end] == temp:
                end += 1
            else:
                temp = nums[end]
                start += 1
                nums[start] = temp
                end += 1
        return start + 1

if __name__ == '__main__':
    n = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(n))
    print(n)