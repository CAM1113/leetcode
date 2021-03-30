from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(preorder: List[int], inorder: List[int], idx: int):
    val = preorder[idx[0]]
    idx[0] += 1

    root = TreeNode(val)
    if len(inorder) == 0:
        return root
    index = 0
    while inorder[index] != val:
        index += 1
    left = None
    if index != 0:
        left_inorder = inorder[0:index]
        left = dfs(preorder, left_inorder, idx)
    right = None
    if index != len(inorder) - 1:
        right_inorder = inorder[index + 1:]
        right = dfs(preorder, right_inorder, idx)
    root.left = left
    root.right = right
    return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return dfs(preorder, inorder, [0])


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(Solution().buildTree(preorder, inorder))
