class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a = 0
        b = 1
        index = 2
        while index < n:
            temp = a + b
            a = b
            b = temp
            index += 1
        return (a + b)%1000000007