from typing import List


# 超时，用dp做
def dfs(s_list: List[str], sub_set, index, current_m, current_n, m, n, max_len):
    if index >= len(s_list):
        if len(sub_set) > max_len[0]:
            max_len[0] = len(sub_set)
        return
    s = s_list[index]
    sm = 0
    sn = 0
    for c in s:
        if c == '0':
            sm += 1
        else:
            sn += 1

    if not (current_m + sm > m or current_n + sn > n):

        sub_set.append(s)
        if len(sub_set) > max_len[0]:
            max_len[0] = len(sub_set)
        current_n += sn
        current_m += sm
        dfs(s_list, sub_set, index + 1, current_m, current_n, m, n, max_len)
        sub_set.pop()
        current_n -= sn
        current_m -= sm
    dfs(s_list, sub_set, index + 1, current_m, current_n, m, n, max_len)


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        max_len = [0]
        dfs(strs, [], 0, 0, 0, m, n, max_len)
        return max_len[0]


if __name__ == '__main__':
    strs = ["10", "0", "1"]
    m = 1
    n = 1
    print(Solution().findMaxForm(strs, m, n))
