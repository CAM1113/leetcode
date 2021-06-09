from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_list = []
        while p is not None:
            p_list.append(p)
            p = p.parent
        while q is not None:
            if q in p_list:
                return q
            q = q.parent
