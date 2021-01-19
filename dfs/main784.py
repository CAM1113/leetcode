from typing import List


def dfs(s, index, results):
    while index < len(s) and '0' <= s[index] <= '9':
        index += 1

    if index == len(s):
        results.append(''.join(s))
        return

    s[index] = str.lower(s[index])
    dfs(s, index + 1, results)

    s[index] = str.upper(s[index])
    dfs(s, index + 1, results)


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if len(S) == 0:
            return []

        s = list(S)
        results = []
        dfs(s, 0, results)
        return results


def main():
    S = "a1b2"
    print(Solution().letterCasePermutation(S))


if __name__ == '__main__':
    main()

