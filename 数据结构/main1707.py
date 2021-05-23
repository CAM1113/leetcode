from typing import List


class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.min_val = 10 ** 9
        self.val = -1


max_bit = 30


def build_tree(root: TreeNode, n):
    binary_list = [0] * max_bit
    index = 0
    _n = n
    while n > 0:
        if n % 2 == 1:
            binary_list[index] = 1
        index += 1
        n //= 2
    binary_list = binary_list[::-1]
    n = _n
    for i in binary_list:
        if n < root.min_val:
            root.min_val = n
        if i == 1:
            if root.right is None:
                root.right = TreeNode()
                root.right.min_val = n
            root = root.right

        else:
            if root.left is None:
                root.left = TreeNode()
                root.left.min_val = n
            root = root.left
    root.val = n


def find_max(root: TreeNode, x: int, m: int):
    n = x
    binary_list = [0] * max_bit
    index = 0
    while n > 0:
        if n % 2 == 1:
            binary_list[index] = 1
        index += 1
        n //= 2
    binary_list = binary_list[::-1]
    for b in binary_list:
        if b == 0:
            if root.right is not None and m >= root.right.min_val:
                root = root.right
                continue
            if root.left is not None and m >= root.left.min_val:
                root = root.left
                continue
        else:
            if root.left is not None and m >= root.left.min_val:
                root = root.left
                continue
            if root.right is not None and m >= root.right.min_val:
                root = root.right
                continue
        return -1

    if root.left is None and root.right is None:
        if m >= root.val:
            return root.val ^ x
        return -1

    return -1


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        root = TreeNode()
        for n in nums:
            build_tree(root, n)
        result = []

        for q in queries:
            x, m = q[0], q[1]
            result.append(find_max(root, x, m))
        return result


if __name__ == '__main__':
    nums =[5,2,4,6,6,3]
    queries = [[12,4],[8,1],[6,3]]
    print(Solution().maximizeXor(nums, queries))
