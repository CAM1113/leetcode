from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        if n == 2:
            return primes[0]
        dp = [1 for _ in range(n)]
        mul_list = [0 for _ in primes]
        index = 1
        while index < n:
            step = [(dp[mul_list[i]]*v, i)  for i, v in enumerate(primes)]
            step = min(step, key=lambda x: x[0])
            if step[0] == dp[index-1]:
                mul_list[step[1]] += 1
                continue
            dp[index] = step[0]
            mul_list[step[1]] += 1
            index += 1
        return dp[-1]


if __name__ == '__main__':
    print(Solution().nthSuperUglyNumber(n=12, primes=[2, 7, 13, 19]))
