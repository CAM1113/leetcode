
def get_count(board,x,y):
    sumed = 0
    if x - 1 >= 0:
        if y - 1 >= 0:
            if board[x-1][y-1] == 'M':
                sumed += 1
        if board[x-1][y] == 'M':
            sumed += 1

        if y+1 < len(board[0]):
            if board[x-1][y+1] == 'M':
                sumed += 1

    if x + 1 < len(board):
        if y - 1 >= 0:
            if board[x+1][y-1] == 'M':
                sumed += 1
        if board[x+1][y] == 'M':
            sumed += 1

        if y+1 < len(board[0]):
            if board[x+1][y+1] == 'M':
                sumed += 1

    if y - 1 >= 0:
        if board[x][y - 1] == 'M':
            sumed += 1

    if y + 1 < len(board[0]):
        if board[x][y + 1] == 'M':
            sumed += 1
    return sumed


def dfs_click(board,x,y):
    if board[x][y] == 'B':
        return

    count = get_count(board,x,y)
    if count > 0:
        board[x][y] = f'{count}'
        return

    board[x][y] = 'B'
    if x-1>=0:
        if y - 1 >= 0 and board[x-1][y-1] != 'M':
            dfs_click(board,x-1,y-1)
        if board[x-1][y] != 'M':
            dfs_click(board,x-1,y)
        if y+1 < len(board[0]) and board[x-1][y+1] != 'M':
            dfs_click(board,x-1,y+1)

    if y - 1 >= 0 and board[x][y - 1] != 'M':
        dfs_click(board, x, y - 1)

    if y + 1 < len(board[0]) and board[x][y + 1] != 'M':
        dfs_click(board, x, y + 1)

    if x+1<len(board):
        if y - 1 >= 0 and board[x+1][y-1] != 'M':
            dfs_click(board,x+1,y-1)
        if board[x+1][y] != 'M':
            dfs_click(board,x+1,y)
        if y+1 < len(board[0]) and board[x+1][y+1] != 'M':
            dfs_click(board,x+1,y+1)
    return board


class Solution:
    def updateBoard(self, board, click):
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        dfs_click(board,click[0],click[1])
        return board
