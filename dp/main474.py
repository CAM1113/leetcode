from typing import List


# m => 0,n=> 1

def getmn(s):
    m = 0
    n = 0
    for c in s:
        if c == "0":
            m += 1
        else:
            n += 1
    return m, n


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # state[i]表示，到i为止，子集的最大长度，m个数，n个数
        states = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for s_index in range(len(strs)):
            ms, ns = getmn(strs[s_index])
            for i in range(m + 1):
                for j in range(n + 1):
                    if i - ms >= 0 and j - ns >= 0:
                        states[s_index + 1][i][j] = max(states[s_index][i - ms][j - ns] + 1, states[s_index][i][j])
                    else:
                        states[s_index + 1][i][j] = states[s_index][i][j]
        return states[-1][-1][-1]


if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(Solution().findMaxForm(strs, m, n))
