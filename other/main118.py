from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        results = []
        for i in range(numRows):
            if i == 0:
                results.append([1])
                continue
            result = []
            for j in range(i + 1):
                if j == 0:
                    result.append(1)
                    continue
                if j == i:
                    result.append(1)
                    continue
                result.append(results[-1][j] + results[-1][j - 1])
            results.append(result)
        return results


if __name__ == '__main__':
    n = 5
    print(Solution().generate(n))
