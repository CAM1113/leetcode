from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        level = [root]
        level_next = []
        results = []
        while len(level) != 0:
            result = []
            for i in level:
                result.append(i.val)
                if i.left is not None:
                    level_next.append(i.left)
                if i.right is not None:
                    level_next.append(i.right)
            results.append(result)
            level = level_next
            level_next = []
        return results
