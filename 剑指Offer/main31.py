class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        pop_index = 0
        while index < len(pushed):
            stack.append(pushed[index])
            while len(stack) > 0 and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
            index += 1
        return len(stack) == 0