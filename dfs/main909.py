from typing import List


def get_rc(state, N):
    state -= 1
    row = state // N
    real_row = (N - 1) - row
    col = state % N
    if row % 2 == 1:
        col = (N - 1) - col
    return real_row, col


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        if board[0][0] != -1:
            level = [board[0][0]]
        else:
            level = [1]
        used = set()
        N = len(board)
        target = N ** 2
        step = 0

        while len(level) != 0:
            step += 1
            next_level = []
            for state in level:
                if state in used:
                    continue
                if state == target:
                    return step - 1
                used.add(state)
                for i in range(1, 7):
                    if state + i > target:
                        break
                    r, c = get_rc(state + i, N)
                    if board[r][c] != -1:
                        next_level.append(board[r][c])
                        continue
                    next_level.append(state + i)
            level = next_level
        return -1


if __name__ == '__main__':
    x = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]]
    print(Solution().snakesAndLadders(x))
