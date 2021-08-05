import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, position, deep, path_dic):
    path_dic[position].append((root.val, deep))
    if root.left is not None:
        dfs(root.left, position - 1, deep + 1, path_dic)
    if root.right is not None:
        dfs(root.right, position + 1, deep + 1, path_dic)


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        path_dic = collections.defaultdict(list)
        dfs(root, 0, 0,path_dic)
        result = []
        keys = list(path_dic.keys())
        keys.sort()
        for k in keys:
            l = path_dic[k]
            l.sort(key=lambda x:(1000-x[1])*10000+x[0])
            result.append()
        return result
