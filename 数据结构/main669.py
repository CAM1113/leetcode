class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode, low: int, high: int):
    if root is None:
        return None
    if root.val < low:
        return dfs(root.right,low,high)
    if root.val > high:
        return dfs(root.right,low,high)

    if low <= root.val <= high:
        left = dfs(root.left, low, high)
        right = dfs(root.right, low, high)
        root.left = left
        root.right = right
        return root


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        return dfs(root, low, high)
