import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode, max_val):
    if root.left is None and root.right is None:
        if root.val > max_val[0]:
            max_val[0] = root.val
        return max(root.val, 0), root.val
    max_left = 0
    max_right = 0
    max_total_v1 = -10000
    max_total_v2 = -10000
    if root.left is not None:
        max_left, max_total_v1 = dfs(root.left, max_val)
    if root.right is not None:
        max_right, max_total_v2 = dfs(root.right, max_val)
    max_v = max(root.val + max_left, root.val + max_right)
    max_total = root.val + max_left + max_right
    if max_v > max_val[0]:
        max_val[0] = max_v
    if max_total > max_val[0]:
        max_val[0] = max_total
    return max(max_v, 0), max(max_total, max_total_v1, max_total_v2)


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_val = [root.val]
        dfs(root, max_val)
        return max_val[0]
