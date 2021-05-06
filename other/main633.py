import math


def is_square(x):
    s = math.sqrt(x)
    return s - int(s) == 0


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_num = math.sqrt(c)
        if is_square(max_num):
            return True
        max_num = int(max_num)
        min_num = c - max_num ** 2
        while max_num**2 >= min_num:
            if is_square(min_num):
                return True
            max_num -= 1
            min_num = c - max_num**2
        return False


if __name__ == '__main__':
    xx = 1000
    print(Solution().judgeSquareSum(xx))
