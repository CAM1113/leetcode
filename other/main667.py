from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k == 1:
            return list(range(1, n + 1))
        if k == 2:
            result = [1, 3, 2]
            for i in range(4, n + 1):
                result.append(i)
            return result

        result = []
        nu = 0
        while len(result) < k - 1:
            result.append(nu + 1)
            result.append(n - nu)
            nu += 1
        while len(result) < n:
            result.append(n - nu)
            nu += 1

        return result


if __name__ == '__main__':
    print(Solution().constructArray(3, 1))
