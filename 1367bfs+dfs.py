# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1367. 二叉树中的列表
# 给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。
# 如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 。
# 一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。
#
# 思路：先用广度优先搜索查找所有可能的root起始点，在对每个起始点做深度优先查找判断是否满足要求
def bfs_get_roots(head, root, heads):
    if root is None:
        return
    if root.val == head.val:
        heads.append(root)
    bfs_get_roots(head, root.left, heads)
    bfs_get_roots(head, root.right, heads)


def dfs_judge_path(head, root):
    if head is None:
        return True
    if root is None:
        return False
    if head.val == root.val:
        return dfs_judge_path(head.next, root.left) or dfs_judge_path(head.next, root.right)
    else:
        return False


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        roots = []
        bfs_get_roots(head, root, heads=roots)
        for r in roots:
            if dfs_judge_path(head, r):
                return True
        return False
