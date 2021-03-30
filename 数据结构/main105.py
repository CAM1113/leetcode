from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
