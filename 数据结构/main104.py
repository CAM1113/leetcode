class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        layer = [root]
        layers = 0
        while len(layer) == 0:
            next_layer = []
            layers += 1
            for r in layer:
                if r.left is not None:
                    next_layer.append(r.left)
                if r.right is not None:
                    next_layer.append(r.right)
            layer = next_layer
        return layers
