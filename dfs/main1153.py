def dfs(n, mem_dict: dict):
    if n in mem_dict.keys():
        return mem_dict[n]
    min_day1 = n % 2 + dfs(n // 2, mem_dict) + 1
    min_day2 = n % 3 + dfs(n // 3, mem_dict) + 1
    min_day = min(min_day1, min_day2)
    mem_dict[n] = min_day
    return min_day


class Solution:
    def minDays(self, n: int) -> int:
        mem_dict = {}
        mem_dict[1] = 1
        mem_dict[2] = 2
        return dfs(n, mem_dict)


if __name__ == '__main__':
    x = 198
    print(Solution().minDays(x))
