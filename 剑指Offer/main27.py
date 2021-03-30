class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(root: TreeNode):
    temp = root.left
    root.left = root.right
    root.right = temp
    if root.left is not None:
        dfs(root.left)
    if root.right is not None:
        dfs(root.right)


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        dfs(root)
        return root
