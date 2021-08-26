import collections
import sys
from typing import List

# 超时
def dfs(paths, start, dst, min_price, current_price, current_k, k, state):
    next_node = paths[start]
    if current_k > k:
        return
    if current_price >= state[start][0] and current_k >= state[start][1]:
        return
    if state[start][0] > current_price and state[start][1] > current_k:
        state[start] = (current_price, current_k)

    for n, p in next_node:
        if n == dst:
            if current_price + p < min_price[0]:
                min_price[0] = current_price + p
            continue
        current_price += p
        dfs(paths, n, dst, min_price, current_price, current_k + 1, k)
        current_price -= p


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        paths = collections.defaultdict(list)
        for f in flights:
            paths[f[0]].append((f[1], f[2]))
        min_price = [sys.maxsize]
        state = [(sys.maxsize, sys.maxsize) for _ in range(n)]
        dfs(paths, src, dst, min_price, 0, 0, k, state)
        if min_price[0] == sys.maxsize:
            return -1
        return min_price[0]


if __name__ == '__main__':
    print(Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                                       src=0, dst=2, k=0))
