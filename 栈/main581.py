from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        start_index = -1
        end_index = -1
        for index, val in enumerate(nums):
            if len(stack) == 0:
                stack.append(val)
                continue
            if val >= stack[-1]:
                stack.append(val)
                continue
            end_index = index

            temp_index = 0
            while temp_index < len(stack) and val >= stack[temp_index]:
                temp_index += 1

            if start_index == -1 or start_index > temp_index-1:
                start_index = temp_index - 1

        if start_index == -1 and end_index == -1:
            return 0

        return end_index - start_index


if __name__ == '__main__':
    print(Solution().findUnsortedSubarray(nums=[1,3,5,4,2]))
