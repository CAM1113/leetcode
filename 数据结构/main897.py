class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, head, tail):
    if root.left is None and root.right is None:
        if head is None:
            return root, root
        else:
            tail.right = root
            tail = root
            return head, tail
    if root.left is not None:
        head, tail = dfs(root.left, head, tail)
    if tail is not None:
        tail.right = root
    else:
        head = root
    tail = root
    root.left = None
    if root.right is not None:
        head, tail = dfs(root.right, head, tail)
    return head, tail


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head, _ = dfs(root, None, None)
        return head


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.right = n2
    print(Solution().increasingBST(n1).val)
