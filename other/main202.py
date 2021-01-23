def next(n):
    result = 0
    while n != 0:
        temp = n % 10
        result += temp ** 2
        n = n // 10
    return result


class Solution:
    def isHappy(self, n: int) -> bool:
        n_set = set()
        while n not in n_set:
            if n == 1:
                return True
            n_set.add(n)
            n = next(n)
        return False
