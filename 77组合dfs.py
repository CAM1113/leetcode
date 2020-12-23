def dfs(n, results, result, start_index, k):
    if len(result) == k:
        results.append(result[0:])
        return

    for i in range(start_index, n, 1):
        result.append(i+1)
        dfs(n, results, result, i+1, k)
        result.pop(-1)


class Solution:
    def combine(self, n: int, k: int):
        results = []
        result = []
        start_index = 0
        dfs(n, results, result, start_index, k)
        return results


def main():
    n = 4
    k = 2
    print(Solution().combine(n, k))


if __name__ == '__main__':
    main()
