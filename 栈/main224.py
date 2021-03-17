from typing import List


def cal(s: List[str]):
    start = 0
    sums = 0
    is_add = True
    idx = 0
    for c in s:
        if c == "+" or c == "-":
            num = ''.join(s[start:idx])
            if len(num) == 0:
                num = 0
            else:
                num = int(num)
            start = idx + 1
            if is_add:
                sums += num
            else:
                sums -= num
            if c == "+":
                is_add = True
            else:
                is_add = False
        idx += 1
    num = ''.join(s[start:idx])
    num = int(num)
    if is_add:
        sums += num
    else:
        sums -= num
    return sums


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        for c in s:
            if c == " ":
                continue
            if c == "(" or c == "+" or c == "-" or "0" <= c <= "9":
                stack.append(c)
            else:
                temp = []
                while stack[-1] != "(":
                    temp.append(stack[-1])
                    stack.pop()
                stack.pop()
                re = cal(temp[::-1])
                if re >= 0:
                    stack.append(f"{re}")
                else:
                    if len(stack) == 0:
                        stack.append('-')

                    elif stack[-1] == "-":
                        stack[-1] = "+"
                    else:
                        stack[-1] = "-"
                    stack.append(f"{abs(re)}")

        return cal(stack)


if __name__ == '__main__':
    x = "(5-(1+(5)))"
    print(Solution().calculate(x))
