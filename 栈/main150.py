from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+' or c == '-' or c == '*' or c == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                if c == "+":
                    stack.append(n1 + n2)
                elif c == "-":
                    stack.append(n2 - n1)
                elif c == '*':
                    stack.append(n2 * n1)
                else:
                    stack.append(int(n2 / n1))
            else:
                stack.append(int(c))
        return stack[-1]


if __name__ == '__main__':
    s =  ["4","13","5","/","+"]
    print(Solution().evalRPN(s))
