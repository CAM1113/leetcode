from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return

        start_index = 0
        end_index = len(nums) - 1
        while start_index < end_index and nums[start_index] == 0:
            start_index += 1
        current_index = start_index

        while start_index < end_index and nums[end_index] == 2:
            end_index -= 1

        while current_index <= end_index and start_index < end_index:
            if nums[current_index] == 0:
                temp = nums[current_index]
                nums[current_index] = nums[start_index]
                nums[start_index] = temp
            elif nums[current_index] == 1:
                current_index += 1
            elif nums[current_index] == 2:
                temp = nums[current_index]
                nums[current_index] = nums[end_index]
                nums[end_index] = temp
            while start_index < end_index and nums[start_index] == 0:
                start_index += 1
            if start_index > current_index:
                current_index = start_index

            while start_index < end_index and nums[end_index] == 2:
                end_index -= 1


def main():
    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)


if __name__ == '__main__':
    main()
