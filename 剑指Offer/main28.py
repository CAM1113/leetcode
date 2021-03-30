class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack1 = [root]
        stack2 = [root]
        while len(stack1) != 0 and len(stack2) == len(stack1):
            root1 = stack1.pop()
            root2 = stack2.pop()
            if root1.val != root2.val:
                return False

            if root1.left is None and root2.right is not None:
                return False
            if root1.left is not None and root2.right is None:
                return False
            if root1.left is not None and root2.right is not None:
                stack1.append(root1.left)
                stack2.append(root2.right)

            if root1.right is None and root2.left is not None:
                return False
            if root1.right is not None and root2.left is None:
                return False
            if root1.right is not None and root2.left is not None:
                stack1.append(root1.right)
                stack2.append(root2.left)

        if len(stack1) == len(stack2) == 0:
            return True
        return False
