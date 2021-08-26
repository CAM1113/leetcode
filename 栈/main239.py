import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        stack = collections.deque()
        stack.append(nums[0])
        result = []
        end = 1
        while end < k:
            while len(stack) > 0 and stack[-1] < nums[end]:
                stack.pop()
            stack.append(nums[end])
            end += 1
        result.append(stack[0])
        while end < len(nums):
            pop_val = nums[start]
            push_val = nums[end]
            start += 1
            end += 1
            if pop_val == stack[0]:
                stack.popleft()
            while len(stack) > 0 and stack[-1] < push_val:
                stack.pop()
            stack.append(push_val)
            result.append(stack[0])
        return result

