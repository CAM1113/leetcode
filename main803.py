# 超时，每次要重复计算连通情况
# def dfs(grid, is_used, current_x, current_y, num_rest):
#     # 坐标范围约束
#     if current_x < 0 or current_x >= len(grid) or current_y < 0 or current_y >= len(grid[0]):
#         return
#         # grid约束
#     if grid[current_x][current_y] == 0 or is_used[current_x][current_y] == 1:
#         return
#     is_used[current_x][current_y] = 1
#     num_rest[0] += 1
#     dfs(grid, is_used, current_x - 1, current_y, num_rest)
#     dfs(grid, is_used, current_x + 1, current_y, num_rest)
#     dfs(grid, is_used, current_x, current_y - 1, num_rest)
#     dfs(grid, is_used, current_x, current_y + 1, num_rest)
# class Solution:
#     def hitBricks(self, grid, hits):
#         results = []
#         num_rest = [0, sum([sum(g) for g in grid])]
#         for hit in hits:
#             is_used = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
#             if grid[hit[0]][hit[1]] == 0:
#                 results.append(0)
#                 continue
#             grid[hit[0]][hit[1]] = 0
#             for i in range(len(grid[0])):
#                 dfs(grid, is_used, 0, i, num_rest)
#             results.append(num_rest[1] - num_rest[0] - 1)
#             num_rest[1] = num_rest[0]
#             num_rest[0] = 0
#             grid = is_used
#         return results


def dfs(grid, copy, is_used, current_x, current_y, array):
    # 坐标范围约束
    if current_x < 0 or current_x >= len(grid) or current_y < 0 or current_y >= len(grid[0]):
        return

    if current_x == 0:
        is_used[current_x][current_y] = 1
        array[0] += 1
        dfs(grid, is_used, current_x - 1, current_y, array)
        dfs(grid, is_used, current_x + 1, current_y, array)
        dfs(grid, is_used, current_x, current_y - 1, array)
        dfs(grid, is_used, current_x, current_y + 1, array)
        return

    # grid约束
    if grid[current_x][current_y] == 0 or is_used[current_x][current_y] == 1:
        return

    is_used[current_x][current_y] = 1
    array[0] += 1
    dfs(grid, is_used, current_x - 1, current_y, array)
    dfs(grid, is_used, current_x + 1, current_y, array)
    dfs(grid, is_used, current_x, current_y - 1, array)
    dfs(grid, is_used, current_x, current_y + 1, array)


class Solution:

    def hitBricks(self, grid, hits):
        results = []
        is_used = [[0 for _ in j] for j in grid]
        num = [0]
        copy = [[i for i in j] for j in grid]
        for h in hits:
            copy[h[0]][h[1]] = 0

        for i in range(len(grid[0])):
            dfs(grid, copy, is_used, 0, i, num)
        hits = hits[::-1]
        for h in hits:
            num = [0]
            grid[h[0]][h[1]] = 1
            dfs(grid, is_used, h[0], h[1], num)
            results.append(num[0] - 1)

        return results[::-1]


def main():
    grid = [[1], [1], [1], [1], [1]]
    hits = [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]
    print(Solution().hitBricks(grid, hits))


if __name__ == '__main__':
    main()
