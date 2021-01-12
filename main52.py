def is_ok(grid, row, col,n):
    for i in range(n):
        if grid[i][col] == 'Q' or grid[row][i] == 'Q':
            return False
        if row + i < n and col + i < n:
            if grid[row + i][col + i] == 'Q':
                return False

        if row - i >= 0 and col - i >= 0:
            if grid[row - i][col - i] == 'Q':
                return False

        if row - i >= 0 and col + i < n:
            if grid[row - i][col + i] == 'Q':
                return False
        if row + i < n and col - i >= 0:
            if grid[row + i][col - i] == 'Q':
                return False

    return True


def put_queen(grid, row, results,n):
    if row >= n:

        results[0] = results[0] +1
        return

    for i in range(n):
        if is_ok(grid, row, i,n):
            grid[row][i] = 'Q'
            put_queen(grid, row + 1, results,n)
            grid[row][i] = '.'


class Solution:
    def totalNQueens(self, n: int) -> int:
        grid = [['.' for _ in range(n)] for _ in range(n)]
        results = [0]
        put_queen(grid, 0, results,n)
        return results[0]