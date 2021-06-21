import re


# 应该用状态机做

def is_int(s):
    if len(s) == 0:
        return False
    for c in s:
        if "0" <= c <= "9":
            continue
        else:
            return False
    return True


# 返回s的状态，小数（1）、整数（0）、非数（-1），不包含正负号和e
def num_type(s):
    ss = s.split(".")
    if len(ss) == 1:
        if is_int(ss[0]):
            return 0
        else:
            return -1
    if len(ss) == 2:
        if len(ss[0]) == 0:
            if len(ss[1]) == 0:
                return -1
            if is_int(ss[1]):
                return 1
        if is_int(ss[0]):
            if len(ss[1]) == 0 or is_int(ss[1]):
                return 1
            return -1
        return -1
    return -1


class Solution:
    def isNumber(self, s: str) -> bool:
        if s.startswith("+") or s.startswith("-"):
            s = s[1:]

        if s[0] == 'e' or s[0] == 'E':
            return False

        if len(s) == 1 and not ("0" <= s[0] <= "9"):
            return False

        ss = re.split("[eE]", s)
        first = num_type(ss[0])
        if first == -1:
            # 第一部分是非数字
            return False

        if len(ss) == 1:
            return True
        if len(ss) == 2:
            t = ss[1]
            if len(t) < 1:
                return False
            if t[0] == "+" or t[0] == "-":
                t = t[1:]
            if len(t) < 1:
                return False
            second = num_type(t)
            # 第二部分必须整数
            if second == 0:
                return True
            else:
                return False
        return False


if __name__ == '__main__':
    x = "4.m"
    print(Solution().isNumber(x))
