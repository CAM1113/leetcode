import collections
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        in_edge = collections.defaultdict(list)
        out_degree = []
        chosen_node = set()
        for index, e in enumerate(graph):
            out_degree.append(len(e))
            if len(e) == 0:
                chosen_node.add(index)
            for i in e:
                in_edge[i].append(index)

        result = []
        while len(chosen_node) != 0:
            temp_chosen_node = []
            for n in chosen_node:
                result.append(n)
                ins = in_edge[n]
                for i in ins:
                    out_degree[i] -= 1
                    if out_degree[i] == 0:
                        temp_chosen_node.append(i)
            chosen_node = temp_chosen_node
        result.sort()
        return result

if __name__ == '__main__':
    x = [[1, 2], [2, 3], [5], [0], [5], [], []]
    print(Solution().eventualSafeNodes(x))