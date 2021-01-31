# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        results = []
        layer = [root]
        while len(layer) != 0:
            last_layer = []
            sumed = 0.0
            for node in layer:
                sumed +=float(node.val)
                if node.left is not None:
                    last_layer.append(node.left)
                if node.right is not None:
                    last_layer.append(node.right)
            results.append(sumed/len(layer) * 1.0)
            layer = last_layer
        return results
