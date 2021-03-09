from typing import List


def is_ok(s: str):
    if len(s) < 2:
        return True
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def dfs(s: str, start: int, result: List[str], results: List[List[str]]):
    if start >= len(s) - 1:
        if start == len(s) - 1:
            result.append(s[start])
            results.append(result[:])
            result.pop()
        else:
            results.append(result[:])
        return

    for i in range(start + 1, len(s)+1):
        temp_s = s[start:i]
        if is_ok(temp_s):
            result.append(temp_s)
            dfs(s, i, result, results)
            result.pop()


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        results = []
        dfs(s, 0, result, results)
        return results


if __name__ == '__main__':
    x ="aab"
    print(Solution().partition(x))
