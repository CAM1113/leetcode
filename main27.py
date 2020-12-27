class Solution:
    def removeElement(self, nums, val: int) -> int:
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                nums.pop(idx)
            else:
                idx += 1
        return len(nums)
