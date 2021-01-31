class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, current_sum, target_sum):
    current_sum += root.val
    if root.left is None and root.right is None:
        if current_sum == target_sum:
            return True
        else:
            return False
    left = False
    if root.left is not None:
        left = dfs(root.left, current_sum, target_sum)
    right = False
    if root.right is not None:
        right = dfs(root.right, current_sum, target_sum)
    return left or right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        current_sum = 0
        return dfs(root, current_sum, targetSum)
