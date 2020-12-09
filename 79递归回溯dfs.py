from typing import List


def dfs(board: List[List[str]], used_list, current_xy, word, find_index):
    if find_index == len(word):
        # 查找到满足条件的
        return True

    find_char = word[find_index]
    x, y = current_xy

    if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
        return False

    if used_list[x][y] == 1:
        return False

    if board[x][y] == find_char:
        used_list[x][y] = 1
        if dfs(board, used_list, (x - 1, y), word, find_index + 1):
            return True
        if dfs(board, used_list, (x + 1, y), word, find_index + 1):
            return True
        if dfs(board, used_list, (x, y - 1), word, find_index + 1):
            return True
        if dfs(board, used_list, (x, y + 1), word, find_index + 1):
            return True

    used_list[x][y] = 0
    return False


class Solution:
    def exist(self, board, word: str) -> bool:
        used_list = [[0 for _ in range(len(x))] for x in board]
        for i in range(len(board)):
            for j in range(len((board[0]))):
                if dfs(board, used_list, (i, j), word, 0):
                    return True
        return False


def main():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word = "ABCB"
    print(Solution().exist(board, word))


if __name__ == '__main__':
    main()
