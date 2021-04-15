class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, lis, min_minus):
    if root is None:
        return
    for n in lis:
        if abs(n - root.val) < min_minus[0]:
            min_minus[0] = abs(n - root.val)
    lis.append(root.val)
    dfs(root.left)
    dfs(root.right)


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        minus = [10 ** 6]
        dfs(root, [], minus)
        return minus[0]
