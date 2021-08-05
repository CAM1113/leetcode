import collections
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        k -= 1
        edges = collections.defaultdict(list)
        for t in times:
            edges[t[0] - 1].append((t[1] - 1, t[2]))
        used_node = {k}
        path_weight = [100 * 100 for _ in range(n)]
        path_weight[k] = 0
        while len(used_node) < n:
            chosen_node_index = -1
            chosen_node_min_weight = 100000
            chosen_start_node = -1
            chosen_path = (-1,-1)
            for start_node in used_node:
                path = edges[start_node]
                p_index = 0
                while p_index < len(path):
                    p = path[p_index]
                    if p[0] in used_node:
                        path.pop(p_index)
                        continue
                    path_weight[p[0]] = min(path_weight[p[0]], path_weight[start_node] + p[1])
                    if path_weight[p[0]] < chosen_node_min_weight:
                        chosen_node_min_weight = path_weight[p[0]]
                        chosen_node_index = p[0]
                        chosen_start_node = start_node
                        chosen_path = p
                    p_index += 1
            if chosen_node_index == -1:
                break
            used_node.add(chosen_node_index)
            edges[chosen_start_node].remove(chosen_path)
        if len(used_node) < n:
            return -1
        else:
            return max(path_weight)


if __name__ == '__main__':
    print(Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
