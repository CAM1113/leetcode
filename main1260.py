import numpy as np


class Solution:
    def shiftGrid(self, grid, k: int):
        grid = np.array(grid)
        m, n = grid.shape
        grid = grid.reshape(-1)
        length = grid.shape[0]
        k = k % length

        head = grid[length - k:]
        tail = grid[:length - k]
        grid = np.concatenate([head, tail], axis=0)
        grid = grid.reshape(m, n)
        return grid
