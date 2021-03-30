from typing import List


def dfs(postorder: List[int]):
    if len(postorder) < 3:
        return True
    root_val = postorder[-1]
    index = 0
    left = []
    while index < len(postorder) - 1:
        if postorder[index] > root_val:
            break
        left.append(postorder[index])
        index += 1

    right = []
    while index < len(postorder) - 1:
        if postorder[index] < root_val:
            return False
        right.append(postorder[index])
        index += 1
    return dfs(left) and dfs(right)


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        return dfs(postorder)


if __name__ == '__main__':
    x = [1, 3, 2, 6, 5]
    print(Solution().verifyPostorder(x))
