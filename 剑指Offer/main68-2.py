class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(root, path, p_path, q_path, p, q):
    if len(p_path) != 0 and len(q_path) != 0:
        return
    path.append(root)
    if root.val == p.val:
        for r in path:
            p_path.append(r)
    if root.val == q.val:
        for r in path:
            q_path.append(r)
    if root.left is not None:
        dfs(root.left, path, p_path, q_path, p, q)
    if root.right is not None:
        dfs(root.right, path, p_path, q_path, p, q)
    path.pop()


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = []
        q_path = []
        dfs(root, [], p_path, q_path, p, q)
        index = 0
        length = min(len(p_path), len(q_path))
        while index < length:
            if p_path[index].val != q_path[index].val:
                break
            index += 1
        return p_path[index - 1]
