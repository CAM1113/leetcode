# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode, results: List[int]):
    if root.left is None and root.right is None:
        results.append(root.val)
        return
    if root.left is not None:
        dfs(root.left, results)
    if root.right is not None:
        dfs(root.right, results)


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        re1 = []
        dfs(root1, re1)
        re2 = []
        dfs(root2, re2)
        if len(re1) == len(re2):
            for i in range(len(re2)):
                if re2[i] != re1[i]:
                    return False
            return True
        return False
