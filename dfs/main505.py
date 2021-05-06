from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        level = [start]
        is_used = [[False for _ in maze[0]] for _ in maze]
        step = 0
        while len(level) != 0:
            next_level = []
            step += 1
            for p in level:
                is_used[p[0]][p[1]] = True
                if p[0] == destination[0] and p[1] == destination[1]:
                    return step

                if p[0] - 1 >= 0 and not is_used[p[0] - 1][p[1]] and maze[p[0] - 1][p[1]] == 0:
                    next_level.append([p[0] - 1, p[1]])

                if p[0] + 1 < len(maze) and not is_used[p[0] + 1][p[1]] and maze[p[0] + 1][p[1]] == 0:
                    next_level.append([p[0] + 1, p[1]])

                if p[1] + 1 < len(maze[0]) and not is_used[p[0]][p[1] + 1] and maze[p[0]][p[1] + 1] == 0:
                    next_level.append([p[0], p[1] + 1])

                if p[1] - 1 >= 0 and not is_used[p[0]][p[1] - 1] and maze[p[0]][p[1] - 1] == 0:
                    next_level.append([p[0], p[1] - 1])
            level = next_level
        return -1
