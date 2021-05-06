class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        first = 0
        second = 1
        index = 2
        while index <= n:
            temp = first + second
            first = second
            second = temp
        return second
