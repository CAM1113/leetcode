def dfs(grid, is_used, star_x, start_y):
    if star_x < 0 or star_x >= len(grid) or start_y < 0 or start_y >= len(grid[0]) \
            or grid[star_x][start_y] == '0' or is_used[star_x][start_y] == True:
        return
    is_used[star_x][start_y] = True
    dfs(grid, is_used, star_x - 1, start_y)
    dfs(grid, is_used, star_x, start_y - 1)
    dfs(grid, is_used, star_x + 1, start_y)
    dfs(grid, is_used, star_x, start_y + 1)


class Solution:
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        is_used = [[False for _ in range(col)] for _ in range(row)]
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and is_used[i][j] == False:
                    dfs(grid, is_used, i, j)
                    count += 1
        return count


def main():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(Solution().numIslands(grid))


if __name__ == '__main__':
    main()
