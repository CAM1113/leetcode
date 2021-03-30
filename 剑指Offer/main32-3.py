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
        result = []
        level = [root]
        index = 0
        while len(level) != 0:

            next_level = []
            re = []
            for n in level:
                re.append(n.val)
                if n.left is not None:
                    next_level.append(n.left)
                if n.right is not None:
                    next_level.append(n.right)
            if index % 2 != 0:
                re.reverse()
            result.append(re)
            index += 1
            level = next_level
        return result
