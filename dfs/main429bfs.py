# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        level = [root]
        result = []
        while len(level) != 0:
            next_level = []
            res = []
            for i in level:
                res.append(i.val)
                if i.children is not None:
                    for c in i.children:
                        next_level.append(c)
            result.append(res)
            level = next_level
        return result
