from typing import List


def dfs(board: List[List[str]], x, y, array, is_used, index):
    if board[x][y] == 'X' or is_used[x][y] == True:
        return
    array[x][y] = index
    is_used[x][y] = True
    if x - 1 >= 0 and is_used[x - 1][y] == False:
        dfs(board, x - 1, y, array, is_used, index)
    if x + 1 < len(board) and is_used[x + 1][y] == False:
        dfs(board, x + 1, y, array, is_used, index)
    if y + 1 < len(board[0]) and is_used[x][y + 1] == False:
        dfs(board, x, y + 1, array, is_used, index)
    if y - 1 >= 0 and is_used[x][y - 1] == False:
        dfs(board, x, y - 1, array, is_used, index)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) == 0 or len(board[0]) == 0:
            return
        is_used = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        array = [[-1 for _ in range(len(board[0]))] for _ in range(len(board))]
        index = 1
        for i in range(len(board)):
            dfs(board, i, 0, array, is_used, index)
            dfs(board, i, len(board[0]) - 1, array, is_used, index)
        for i in range(len(board[0])):
            dfs(board, 0, i, array, is_used, index)
            dfs(board, len(board) - 1, i, array, is_used, index)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if array[i][j] == 1:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
