from typing import List


# 栈使用的经典案例，单调栈！
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(T))]
        for i in range(1, len(T)):
            while len(stack) > 0 and stack[-1][0] < T[i]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([T[i], i])
        return result


if __name__ == '__main__':
    x = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(x))
