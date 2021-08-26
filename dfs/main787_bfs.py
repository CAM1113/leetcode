import collections
import sys
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        paths = collections.defaultdict(list)
        for f in flights:
            paths[f[0]].append((f[1], f[2]))
        state = [sys.maxsize for _ in range(n)]
        state[src] = 0
        level = [src]
        current_k = 0
        while len(level) != 0:
            if current_k > k:
                break
            current_k += 1
            next_level = []
            # 防止在当前轮次中更新了下一轮才能进行的状态，对本轮后续的状态造成干扰
            change_state = collections.defaultdict(lambda: sys.maxsize)
            for start_node in level:
                next_nodes = paths[start_node]
                for nd in next_nodes:
                    if state[start_node] + nd[1] < change_state[nd[0]]:
                        change_state[nd[0]] = state[start_node] + nd[1]
                        if nd[0] != dst:
                            next_level.append(nd[0])
            for kk in change_state.keys():
                v = change_state[kk]
                if state[kk] > v:
                    state[kk] = v
            level = next_level
        if state[dst] == sys.maxsize:
            return -1
        return state[dst]


if __name__ == '__main__':
    print(Solution().findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))
