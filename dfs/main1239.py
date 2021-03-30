from typing import List


def dfs(arr, index: int, max_len: list, lis_set: set):
    if index>= len(arr):
        return
    word = set(arr[index])
    if len(word) != len(arr[index]) or len(word.intersection(lis_set)) != 0:
        dfs(arr, index + 1, max_len, lis_set)
    else:
        for w in word:
            lis_set.add(w)
        if max_len[0] < len(lis_set):
            max_len[0] = len(lis_set)
        dfs(arr, index + 1, max_len, lis_set)
        for w in word:
            lis_set.remove(w)
        dfs(arr, index + 1, max_len, lis_set)


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = [0]
        lis_set = set()
        dfs(arr, 0, max_len, lis_set)
        return max_len[0]


if __name__ == '__main__':
    arr = ["cha", "r", "act", "ers"]
    print(Solution().maxLength(arr))
