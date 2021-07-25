import collections
from typing import List


def dfs(s: str, wordDict: set, start: int, cache: dict):
    if start >= len(s):
        cache[start] = ""

    for i in range(start, len(s) + 1):
        if s[start:i] in wordDict:
            if len(cache[i]) != 0:
                cache[start] += [s[start:i] + " " + ll for ll in cache[i]]
                continue
            dfs(s, wordDict, i, cache)

            if len(cache[i]) != 0:
                cache[start] += [s[start:i] + " " + ll for ll in cache[i]]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = collections.defaultdict(list)
        cache[len(s)] = [""]
        dfs(s, wordDict, 0, cache)
        return [s.strip() for s in cache[0]]


if __name__ == '__main__':
    print(Solution().wordBreak(
        s="catsanddog",
        wordDict=["cat", "cats", "and", "sand", "dog"]
    ))
