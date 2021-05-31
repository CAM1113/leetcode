class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ")":
                temp = []
                while len(stack)>0 and stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack += temp
                continue
            stack.append(c)
        return "".join(stack)