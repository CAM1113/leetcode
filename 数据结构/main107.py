from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        next_visit = [root]
        results = []
        while len(next_visit) != 0:
            result = []
            new_next = []
            for r in next_visit:
                result.append(r.val)
                if r.left is not None:
                    new_next.append(r.left)
                if r.right is not None:
                    new_next.append(r.right)
            results.append(result)
            next_visit = new_next
        return results
