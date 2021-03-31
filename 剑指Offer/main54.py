# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(root: TreeNode, result: list, k):
    if len(result) == k:
        return
    if root.right is not None:
        dfs(root.right, result, k)
    if len(result) == k:
        return
    result.append(root.val)
    if len(result) == k:
        return
    if root.left is not None:
        dfs(root.left, result, k)


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        red = []
        dfs(root, red, k)
        return red[-1]