# 50. Pow(x, n)
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.do_pow(x, -n)
        else:
            return self.do_pow(x, n)

    def do_pow(self, x, n):
        if n == 1:
            return x
        y = self.do_pow(x, n / 2)
        if n % 2 == 0:
            return y * y
        else:
            return y * y * x
