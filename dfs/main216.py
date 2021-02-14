from typing import List


def dfs(start, result: List, results: List, k, n):
    if len(result) == k:
        if sum(result) == n:
            results.append(result[:])
        return
    if sum(result) >= n:
        return
    for i in range(start, 10):
        result.append(i)
        dfs(i + 1, result, results, k, n)
        result.pop()


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        results = []
        dfs(1, result, results, k, n)
        return results
