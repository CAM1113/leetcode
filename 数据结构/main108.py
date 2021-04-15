from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(nums: List):
    if len(nums) == 1:
        return TreeNode(nums[0])
    if len(nums) == 2:
        return TreeNode(nums[0], right=TreeNode(nums[1]))
    index = len(nums) // 2
    left = dfs(nums[:index])
    right = dfs(nums[index + 1:])
    t = TreeNode(nums[index])
    t.left = left
    t.right = right
    return t


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return dfs(nums)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    print(Solution().sortedArrayToBST(nums))
