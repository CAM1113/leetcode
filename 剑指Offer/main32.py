class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        level = [root]
        res = []
        while len(level) != 0:
            next_level= []
            for n in level:
                res.append(n.val)
                if n.left is not None:
                    next_level.append(n.left)
                if n.right is not None:
                    next_level.append(n.right)
            level = next_level
        return res