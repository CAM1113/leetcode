class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_val(x):
    temp = 0
    for i in x:
        temp = temp * 10 + i
    return temp


def dfs(root: TreeNode, result, results):
    if root is None:
        return
    if root.left is None and root.right is None:
        result.append(root.val)
        results[0] += get_val(result)
        result.pop()
        return
    result.append(root.val)
    if root.left is not None:
        dfs(root.left, result, results)
    if root.right is not None:
        dfs(root.right, result, results)
    result.pop()


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = []
        results = [0]
        dfs(root, result, results)
        return results[0]


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    print(Solution().sumNumbers(a))
