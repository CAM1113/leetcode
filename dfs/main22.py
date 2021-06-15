from typing import List


def dfs(n: int, left: int, right: int, result: List[str], current: str):
    if left == n and right == n:
        result.append(current)
        return
    if left < n:
        dfs(n, left + 1, right, result, current + "(")
    if left > right:
        dfs(n, left, right + 1, result, current + ")")


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        dfs(n, 0, 0, result, "")
        return result
