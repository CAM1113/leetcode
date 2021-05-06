def dfs(n: int, mem_dict):
    if n in mem_dict.keys():
        return mem_dict[n]
    if n == 0:
        return 1
    if n <= 2:
        mem_dict[n] = n
        return n
    total = 0
    for i in range(n):
        le = dfs(i, mem_dict)
        ri = dfs(n - i - 1, mem_dict)
        total += le * ri
    mem_dict[n] = total
    return total


class Solution:
    def numTrees(self, n: int) -> int:
        return dfs(n, {})


if __name__ == '__main__':
    x = 3
    print(Solution().numTrees(x))
