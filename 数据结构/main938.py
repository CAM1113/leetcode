class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0
        stack = [root]
        sums = 0
        while len(stack) != 0:
            r = stack.pop()
            if low <= r.val <= high:
                sums += r
                if r.right is not None:
                    stack.append(r.right)

                if r.left is not None:
                    stack.append(r.left)
                continue

            if r.val < low:
                if r.right is not None:
                    stack.append(r.right)
                continue

            if r.val > high:
                if r.left is not None:
                    stack.append(r.left)
                continue
        return sums
