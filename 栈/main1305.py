import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def put_element(array: collections.deque, root: TreeNode):
    array.append(root)
    if root.left is not None:
        put_element(array, root.left)


def get_element(array: collections.deque):
    e = array[-1]
    array.pop()
    if e.right is not None:
        put_element(array, e.right)


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        array1 = collections.deque()
        array2 = collections.deque()
        if root1 is not None:
            put_element(array1, root1)
        if root2 is not None:
            put_element(array2, root2)
        result = []
        while len(array1) > 0 or len(array2) > 0:
            choose_array = array1
            if len(array1) == 0 and len(array2) != 0:
                choose_array = array2
            if len(array1) != 0 and len(array2) != 0 and array2[-1].val < array1[-1].val:
                choose_array = array2

            val = choose_array[-1].val
            result.append(val)
            get_element(choose_array)
        return result
