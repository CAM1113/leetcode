from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(root, node_info, target, k, result, distance, is_back):
    if root is None:
        return

    if is_back:
        if distance == 0:
            result.append(root.val)
            return
        if root.val not in node_info.keys():
            return
        parent, flag = node_info[root.val]
        if flag == "L":
            dfs(parent.right, node_info, target, k, result, distance - 2, False)
        else:
            dfs(parent.left, node_info, target, k, result, distance - 2, False)
        dfs(parent, node_info, target, k, result, distance - 1, True)
        return

    if root.val == target.val:
        distance = k
        if distance != 0:
            dfs(root, node_info, target, k, result, k, True)

    if distance == 0:
        result.append(root.val)
        return

    if root.left is not None:
        node_info[root.left.val] = (root, "L")
        dfs(root.left, node_info, target, k, result, distance - 1, False)

    if root.right is not None:
        node_info[root.right.val] = (root, "R")
        dfs(root.right, node_info, target, k, result, distance - 1, False)


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        node_info = {}
        result = []
        distance = -1
        dfs(root, node_info, target, k, result, distance, False)
        return result


if __name__ == '__main__':
    n1 = TreeNode(3)
    n2 = TreeNode(5)
    n3 = TreeNode(1)
    n4 = TreeNode(6)
    n5 = TreeNode(2)
    n6 = TreeNode(0)
    n7 = TreeNode(8)
    n8 = TreeNode(7)
    n9 = TreeNode(4)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n5.left = n8
    n5.right = n9

    print(Solution().distanceK(n1, n2, 2))
