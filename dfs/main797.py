from typing import List


def dfs(start, graph, path, current_path):
    current_path.append(start)
    if start == len(graph)-1:
        path.append(current_path[:])
        current_path.pop()
        return
    nodes = graph[start]
    for node in nodes:
        dfs(node, graph, path, current_path)
    current_path.pop()


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        dfs(0, graph, result, [])
        return result


if __name__ == '__main__':
    print(Solution().allPathsSourceTarget(
        graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]
    ))
