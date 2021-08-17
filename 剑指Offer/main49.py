class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        two = 0
        three = 0
        five = 0
        for i in range(1, n):
            v_two = dp[two] * 2
            v_three = dp[three] * 3
            v_five = dp[five] * 5
            v = min(v_two,v_three,v_five)
            dp[i] =v
            if v_two == v:
                two += 1
            if v_three == v:
                three += 1
            if v_five == v:
                five += 1
        return dp[-1]

if __name__ == '__main__':
    print(Solution().nthUglyNumber(10))