from typing import List


def dfs(board: List[List[str]], word: str, current_index, current_Position, is_used):
    if current_index == len(word) - 1:
        return True
    cr = current_Position[0]
    cl = current_Position[1]
    is_used[cr][cl] = True
    if 0 < current_Position[0] and not is_used[cr - 1][cl] and board[cr - 1][cl] == word[current_index + 1]:
        if dfs(board, word, current_index + 1, (cr - 1, cl), is_used):
            return True

    if current_Position[0] < len(board) - 1 and not is_used[cr + 1][cl] and board[cr + 1][cl] == word[
        current_index + 1]:
        if dfs(board, word, current_index + 1, (cr + 1, cl), is_used):
            return True

    if 0 < current_Position[1] and not is_used[cr][cl - 1] and board[cr][cl - 1] == word[current_index + 1]:
        if dfs(board, word, current_index + 1, (cr, cl - 1), is_used):
            return True

    if current_Position[1] < len(board[0]) - 1 and not is_used[cr][cl + 1] and board[cr][cl + 1] == word[
        current_index + 1]:
        if dfs(board, word, current_index + 1, (cr, cl + 1), is_used):
            return True

    is_used[cr][cl] = False
    return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return False
        is_used = [[False for _ in board[0]] for _ in board]
        # for idx, s in enumerate(board[0]):
        #     if s == word[0]:
        #         if dfs(board, word, 0, (0, idx), is_used):
        #             return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(board, word, 0, (i, j), is_used):
                        return True

        return False


if __name__ == '__main__':
    b = [["a", "b"], ["c", "d"]]
    w = "cdba"
    print(Solution().exist(b, w))
