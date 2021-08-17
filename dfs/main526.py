import collections


def dfs(n, is_used, index_val_dic, current_list, result):
    if len(current_list) == n:
        result[0] += 1
        return
    for i in range(n):
        if not is_used[i] and i+1 in index_val_dic[len(current_list) + 1]:
            current_list.append(i)
            is_used[i] = True
            dfs(n, is_used, index_val_dic, current_list, result)
            current_list.pop()
            is_used[i] = False


class Solution:
    def countArrangement(self, n: int) -> int:
        index_val_dic = collections.defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    index_val_dic[i].append(j)
        is_used = [False for _ in range(n)]
        result = [0]
        dfs(n, is_used, index_val_dic, [], result)
        return result[0]


if __name__ == '__main__':
    x = 3
    print(Solution().countArrangement(x))
