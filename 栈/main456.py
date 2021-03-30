from typing import List


# 暴力
class Solution1:
    def find132pattern(self, nums: List[int]) -> bool:
        min_left = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min_left:
                min_left = nums[i]
                continue
            for j in range(i + 1, len(nums)):
                if min_left < nums[j] < nums[i]:
                    return True
        return False


# 单调栈

class Soluti on:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min_left = []
        min_val = nums[0]
        for val in nums:
            if val < min_val:
                min_val = val
            min_left.append(min_val)
        stack = [len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            while len(stack) > 0 and stack[-1] < nums[i]:
                stack.pop()
            if len(stack) == 0:
                continue
            if stack[-1] > min_left[i]:
                return True
            stack.append(nums[i])
        return False


if __name__ == '__main__':
    s = [3,1,4,2]
    print(Solution().find132pattern(s))
