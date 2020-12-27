def dfs(grid, is_used, position, is_click, result):
    result.append(position)
    is_used[position[0]][position[1]] = True
    if position[0] == 0:
        is_click[0] = False
    if position[0] - 1 >= 0 and grid[position[0] - 1][position[1]] == 1 and not is_used[position[0] - 1][position[1]]:
        dfs(grid, is_used, [position[0] - 1, position[1]], is_click, result)

    if position[0] + 1 < len(grid) and grid[position[0] + 1][position[1]] == 1 and not is_used[position[0] + 1][
        position[1]]:
        dfs(grid, is_used, [position[0] + 1, position[1]], is_click, result)

    if position[1] - 1 >= 0 and grid[position[0]][position[1] - 1] == 1 and not is_used[position[0]][position[1] - 1]:
        dfs(grid, is_used, [position[0], position[1] - 1], is_click, result)

    if position[1] + 1 < len(grid[0]) and grid[position[0]][position[1] + 1] == 1 and not is_used[position[0]][
        position[1] + 1]:
        dfs(grid, is_used, [position[0], position[1] + 1], is_click, result)


def dfs2(grid, grid_copy, num, position):
    num[0] = num[0] + 1
    grid[position[0]][position[1]] = 1
    if position[0] - 1 >= 0 and grid_copy[position[0] - 1][position[1]] == 1 and grid[position[0] - 1][
        position[1]] == 0:
        dfs2(grid, grid_copy, num, [position[0] - 1, position[1]])

    if position[0] + 1 < len(grid) and grid_copy[position[0] - 1][position[1]] == 1 and grid[position[0] + 1][
        position[1]] == 0:
        dfs2(grid, grid_copy, num, [position[0] + 1, position[1]])

    if position[1] - 1 >= 0 and grid_copy[position[0]][position[1] - 1] == 1 and grid[position[0]][
        position[1] - 1] == 0:
        dfs2(grid, grid_copy, num, [position[0], position[1] - 1])

    if position[1] + 1 < len(grid[0]) and grid_copy[position[0]][position[1] + 1] == 1 and grid[position[0]][
        position[1] + 1] == 0:
        dfs2(grid, grid_copy, num, [position[0], position[1] + 1])


class Solution:
    def hitBricks(self, grid, hits):
        results = []
        is_used = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        grid_copy = [[a for a in aa] for aa in grid]

        for hit in hits:
            grid[hit[0]][hit[1]] = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                is_click = [True]
                click_positions = []
                dfs(grid, is_used, [i, j], is_click, click_positions)
                if is_click[0]:
                    for p in click_positions:
                        grid[p[0]][p[1]] = 0
        hits = hits[::-1]
        for hit in hits:
            grid[hit[0]][hit[1]] = 1n  
            num = [0]
            dfs2(grid, grid_copy, num, hit)
            results.append(num[0] - 1)

        return results[::-1]


def main():
    grids_ = [[1, 0, 1], [1, 1, 1]]
    hits_ = [[0, 0], [0, 2], [1, 1]]
    print(Solution().hitBricks(grids_, hits_))


if __name__ == '__main__':
    main()
