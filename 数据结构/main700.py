class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val == val:
            return root
        if root.left is not None and val < root.val:
            return self.searchBST(root.left, val)

        if root.right is not None and val > root.val:
            return self.searchBST(root.right, val)
        return None
