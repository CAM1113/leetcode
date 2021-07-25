from typing import List


def get_hash(p):
    return p[0] * 10000 + p[1]


def get_left(maze, start):
    x, y = start
    while y >= 0 and maze[x][y] != 1:
        y -= 1
    return x, y + 1


def get_right(maze, start):
    x, y = start
    while y < len(maze[0]) and maze[x][y] != 1:
        y += 1
    return x, y - 1


def get_top(maze, start):
    x, y = start
    while x >= 0 and maze[x][y] != 1:
        x -= 1
    return x + 1, y


def get_down(maze, start):
    x, y = start
    while x < len(maze) and maze[x][y] != 1:
        x += 1
    return x - 1, y


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        t = [[1 for _ in range(len(maze[0]) + 2)]]
        for i in maze:
            t.append([1])
            for j in i:
                t[-1].append(j)
            t[-1].append(1)
        t.append([1 for _ in range(len(maze[0]) + 2)])
        maze = t
        start[0] += 1
        start[1] += 1
        destination[0] += 1
        destination[1] += 1

        if maze[destination[0] - 1][destination[1]] != 1 and maze[destination[0] + 1][destination[1]] != 1 and \
                maze[destination[0]][destination[1] - 1] != 1 and maze[destination[0]][destination[1] + 1] != 1:
            return False

        level = [start]
        visited_set = set()
        while len(level) != 0:
            next_level = []
            for p in level:
                if p[0] == destination[0] and p[1] == destination[1]:
                    return True
                visited_set.add(get_hash(p))
                p_left = get_left(maze, p)
                if get_hash(p_left) not in visited_set:
                    next_level.append(p_left)
                p_right = get_right(maze, p)
                if get_hash(p_right) not in visited_set:
                    next_level.append(p_right)
                p_top = get_top(maze, p)
                if get_hash(p_top) not in visited_set:
                    next_level.append(p_top)
                p_down = get_down(maze, p)
                if get_hash(p_down) not in visited_set:
                    next_level.append(p_down)
            level = next_level
        return False


if __name__ == '__main__':
    print(Solution().hasPath(
        maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4],
        destination=[4, 4]
    ))
