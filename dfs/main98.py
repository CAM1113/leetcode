import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode, min_val, max_val):
    left = True
    if root.left is not None:
        left = dfs(root.left, min_val, root.val)

    right = True
    if root.right is not None:
        right = dfs(root.right, root.val, max_val)

    return min_val < root.val < max_val and left and right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return dfs(root, -sys.maxsize, sys.maxsize)
