class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level = [(root, 0)]
        mark = False
        father_val = 0
        brother_val = 0
        while len(level) > 0:
            next_level = []
            for n in level:
                if n[0].val == x or n[0].val == y:
                    if mark == False:
                        mark = True
                        father_val = n[1]
                        brother_val = n[1]
                    else:
                        if father_val == n[1] and n[0].val != brother_val:
                            return False
                        else:
                            return True
                if n[0].left is not None:
                    next_level.append((n[0].left, n[0].val))
                if n[0].right is not None:
                    next_level.append((n[0].right, n[0].val))
            if mark == True:
                return False
            level = next_level
        return False
