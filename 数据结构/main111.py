class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        deep = 1
        next_list = [root]
        while len(next_list) != 0:
            new_next = []
            for r in next_list:
                if r.left is None and r.right is None:
                    return deep
                if r.left is not None:
                    new_next.append(r.left)
                if r.right is not None:
                    new_next.append(r.right)
            deep += 1
            next_list = new_next
