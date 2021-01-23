class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(root, is_left, sum):
    if root is None:
        return
    if root.left is not None:
        dfs(root.left, True, sum)
    if root.right is not None:
        dfs(root.right, False, sum)
    if root.left is None and root.right is None and is_left:
        sum[0] += root.val
        return



class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = [0]
        dfs(root, False, sum)
        return sum[0]
