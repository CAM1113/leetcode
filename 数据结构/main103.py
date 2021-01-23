# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        result = []
        results = []
        start_nodes = [root]
        layer = 0
        while True:
            result.clear()
            start_nodes_temp = start_nodes[:]
            start_nodes.clear()
            if len(start_nodes) == 0:
                break
            if layer % 2 == 0:
                # 从左往右遍历
                start_nodes_temp = start_nodes_temp[::-1]
                for node in start_nodes_temp:
                    result.append(node.val)
                    if node.left is not None:
                        start_nodes.append(node.left)
                    if node.right is not None:
                        start_nodes.append(node.right)

            if layer % 2 != 0:
                # 从右往左遍历
                start_nodes_temp = start_nodes_temp[::-1]
                for node in start_nodes_temp:
                    result.append(node.val)
                    if node.right is not None:
                        start_nodes.append(node.right)
                    if node.left is not None:
                        start_nodes.append(node.left)
            results.append(result[:])
            return results
