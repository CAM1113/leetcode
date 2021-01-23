# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, result):
    if root is None:
        return
    dfs(root.left, result)
    dfs(root.right, result)
    result.append(root.val)


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        re = []
        dfs(root, re)
        return re
