from typing import List


def is_ok(board, is_put):
    for i in range(3):
        for j in range(3):
            if board[i][j] != is_put[i][j]:
                return False
    return True


def is_row_ok(is_put, position, mark):
    for i in range(3):
        if is_put[position[0]][i] != mark:
            return False
    return True


def is_col_ok(is_put, position, mark):
    for i in range(3):
        if is_put[i][position[1]] != mark:
            return False
    return True


def is_left_ok(is_put, position, mark):
    for i in range(3):
        if is_put[i][i] != mark:
            return False
    return True


def is_right_ok(is_put, position, mark):
    for i in range(3):
        if is_put[i][2 - i] != mark:
            return False
    return True


def is_over(is_put, position, mark):
    r = is_row_ok(is_put, position, mark) or is_col_ok(is_put, position, mark)
    r = r or is_right_ok(is_put, position, mark) or is_left_ok(is_put, position, mark)
    return r


def dfs(board, put_board, is_x):
    if is_ok(board, put_board):
        return True
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                continue
            if is_x and board[i][j] == 'X' and put_board[i][j] == ' ':
                put_board[i][j] = 'X'
                t = is_over(put_board, (i, j), 'X')
                if t:
                    if is_ok(board, put_board):
                        return True
                    else:
                        put_board[i][j] = ' '
                        continue
                result = dfs(board, put_board, False)
                if result:
                    return True
                put_board[i][j] = ' '

            if not is_x and board[i][j] == 'O' and put_board[i][j] == ' ':
                put_board[i][j] = 'O'
                t = is_over(put_board, (i, j), 'O')
                if t:
                    if is_ok(board, put_board):
                        return True
                    else:
                        put_board[i][j] = ' '
                        continue
                result = dfs(board, put_board, True)
                if result:
                    return True
                put_board[i][j] = ' '
    return False


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        put_board = [[' ', ' ', ' '] for _ in range(3)]
        return dfs(board, put_board, True)


if __name__ == '__main__':
    board = ["XXO", "XOX", "OXO"]
    print(Solution().validTicTacToe(board))
