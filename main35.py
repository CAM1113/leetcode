class Solution:
    def searchInsert(self, nums, target: int) -> int:

        if len(nums) == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1

        start = 0
        end = len(nums) - 1

        if target <= nums[start]:
            return 0
        if target >= nums[-1]:
            return end + 1

        while start < end - 1:
            new_index = (start + end) // 2
            if nums[new_index] == target:
                return new_index
            if nums[new_index] < target:
                start = new_index
            else:
                end = new_index
        return start + 1


if __name__ == '__main__':
    x = [1, 3, 5, 6]
    t = 2
    print(Solution().searchInsert(x, t))
