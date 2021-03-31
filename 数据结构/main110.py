# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode):
    if root.left is None and root.right is None:
        return True, 1
    left_ban = True
    left_deep = 0
    if root.left is not None:
        left_ban, left_deep = dfs(root.left)

    right_ban = True
    right_deep = 0
    if root.right is not None:
        right_ban, right_deep = dfs(root.right)

    if right_ban and left_ban and abs(left_deep - right_deep) <= 1:
        return True, max(left_deep, right_deep) + 1

    return False, 0


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        re, _ = dfs(root)
        return re
