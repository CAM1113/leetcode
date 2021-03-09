from typing import List


# dfs超时
def dfs(s: set, start, word_dic):
    if start >= len(s):
        return True

    for i in range(start, len(s) + 1):
        if s[start:i] in word_dic:
            re = dfs(s, i, word_dic)
            if re:
                return re

    return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dic = set(wordDict)
        return dfs(s, 0, word_dic)


if __name__ == '__main__':
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(Solution().wordBreak(s, wordDict))
