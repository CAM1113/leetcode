from typing import List


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0:
            return False
        word_dic = set(wordDict)
        n = len(s)
        ws = [len(w) for w in word_dic]
        min_len = min(ws)
        max_len = max(ws)
        word_matrix = [[False] * n for _ in range(n)]
        for j in range(min_len, 1 + n):
            start = max(0, j - max_len)
            for i in range(start, j):
                if j - i < min_len:
                    break
                if s[i:j] in word_dic:
                    word_matrix[i][j - 1] = True
        level_set = set()
        level_set.add(0)
        already_set = set()
        while len(level_set) != 0:
            next_level = set()
            for idx in level_set:
                already_set.add(idx)
                for i, b in enumerate(word_matrix[idx]):
                    if b and i + 1 not in already_set and i + 1 not in level_set:
                        if i == n - 1:
                            return True
                        next_level.add(i + 1)
            level_set = next_level
        return False


# dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        wordDict = set(wordDict)
        for i in range(1, n + 1):
            for j in range(i):
                print(j, i)
                if j == 0 and s[j:i] in wordDict:
                    dp[i - 1] = True
                    break

                elif dp[j - 1] and s[j:i] in wordDict:
                    dp[i - 1] = True
                    break
        return dp[-1]


if __name__ == '__main__':
    s = "abbc"
    wordDict = ["ab", "bc"]
    print(Solution().wordBreak(s, wordDict))
