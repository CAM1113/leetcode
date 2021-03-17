class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        index = 0
        last_mark = "+"
        s = s + "+"
        while index < len(s):
            c = s[index]
            if c == ' ':
                index += 1
                continue
            if c == "+" or c == '-' or c == '*' or c == '/':
                temp = []
                while len(stack) > 0 and '0' <= stack[-1] <= '9':
                    temp.append(stack[-1])
                    stack.pop()
                n = int(''.join(temp[::-1]))
                stack.append(n)
                if last_mark == "*":
                    n1 = stack[-1]
                    stack.pop()
                    stack.pop()
                    stack[-1] = stack[-1] * n1

                if last_mark == "/":
                    n1 = stack[-1]
                    stack.pop()
                    stack.pop()
                    stack[-1] = int(stack[-1] / n1)
                last_mark = c
                stack.append(c)
            else:
                stack.append(c)
            index += 1
        stack.pop()
        last_mark = '+'
        sums = 0
        for x in stack:
            if type(x) is int:
                if last_mark == "+":
                    sums += x
                else:
                    sums -= x
                continue
            if x == '+':
                last_mark = "+"
            else:
                last_mark = "-"
        return sums


if __name__ == '__main__':
    s = "3+2*2"
    print(Solution().calculate(s))
