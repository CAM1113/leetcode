class Solution:
    def removeElement(self, nums, val: int) -> int:
        current_position = 0
        current_index = 0
        while current_index < len(nums):
            if nums[current_index] != val:
                nums[current_position] = nums[current_index]
                current_position += 1
            current_index += 1
        return current_position
