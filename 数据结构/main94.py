# 94. 二叉树的中序遍历
# 给定一个二叉树，返回它的中序 遍历。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def inorder(node, lis):
    if node is None:
        return
    inorder(node.left)
    lis.append(node.val)
    inorder(node.right)


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lis = []
        inorder(root, lis)
        return lis
