from typing import List


def dfs(ss, is_used, result, results):
    if len(result) == len(ss):
        results.append(''.join(result))
        return
    i = 0
    while i < len(ss):
        if is_used[i] == True:
            i += 1
            continue
        c = ss[i]
        result.append(c)
        is_used[i] = True
        dfs(ss, is_used, result, results)
        result.pop()
        is_used[i] = False
        while i < len(ss) and ss[i] == c:
            i += 1


class Solution:
    def permutation(self, s: str) -> List[str]:
        s = list(s)
        s.sort()
        result = []
        results = []
        is_used = [False] * len(s)
        dfs(s, is_used, result, results)
        return results
