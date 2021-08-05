# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution2:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1
        level = [root]
        deep = 1
        vals = set()
        while len(level) > 0 and deep < 4:
            next_level = []
            for n in level:
                vals.add(n.val)
                if n.left is not None:
                    next_level.append(n.left)
                if n.right is not None:
                    next_level.append(n.right)
            level = next_level
            deep += 1
        vals = list(vals)
        if len(vals)<2:
            return -1
        vals.sort()
        return vals[1]

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1
        vals = set()
        vals.add(root.val)
        level = [root]
        while len(level)>0:
            next_level = []
            for n in level:
                left = n.left
                right = n.right
                if left is None or right is None:
                    continue
                vals.add(left.val)
                vals.add(right.val)
                if left.val == root.val:
                    next_level.append(left)
                if right.val == root.val:
                    next_level.append(right)
            level = next_level
        vals = list(vals)
        if len(vals)<2:
            return -1
        vals.sort()
        return vals[1]
