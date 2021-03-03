from typing import List


# 单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        i = 0
        sums = 0
        while i < len(height):
            if len(stack) == 0 or height[i] <= stack[-1]:
                stack.append(height[i])
                i += 1
                continue
            temp_height = min(stack[0], height[i])
            temp_index = len(stack) - 1
            while temp_index > 0:
                if temp_height > stack[temp_index]:
                    sums += temp_height - stack[temp_index]
                    stack[temp_index] = temp_height
                    temp_index -= 1
                else:
                    break
            if stack[0] == temp_height:
                stack.clear()
            stack.append(height[i])
            i += 1
        return sums


if __name__ == '__main__':
    h = [4, 2, 0, 3, 2, 5]
    print(Solution().trap(h))
