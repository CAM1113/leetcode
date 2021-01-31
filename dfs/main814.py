class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root):
    if root.left is None and root.right is None:
        return root.val == 1
    left = False
    if root.left is not None:
        left = dfs(root.left)
    if left is False:
        root.left = None

    right = False
    if root.right is not None:
        right = dfs(root.right)
    if right is False:
        root.right = None
    return root.val == 1 or left or right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        if dfs(root) is False:
            return None
        return root
