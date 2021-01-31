class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_find(root, val):
    if root is None:
        return
    val[0] = root
    dfs_find(root.left, val)
    dfs_find(root.right, val)


def find_right(root):
    val = [None]
    dfs_find(root, val)
    return val[0]


def dfs(root):
    if root.left is None and root.right is None:
        return
    if root.left is None:
        dfs(root.right)
    else:
        final_right = find_right(root.left)
        right = root.right
        root.right = root.left
        root.left = None
        final_right.right = right
        dfs(root.right)


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return
        dfs(root)
