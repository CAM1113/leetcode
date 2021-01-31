from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, result, target, results):
    result.append(root.val)
    if root.left is None and root.right is None:
        if sum(result) == target:
            results.append(result[:])
    if root.left is not None:
        dfs(root.left, result, target, results)
    if root.right is not None:
        dfs(root.right, result, target, results)
    result.pop()


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        result = []
        results = []
        dfs(root, result, targetSum, results)
        return results
