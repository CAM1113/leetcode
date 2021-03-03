class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = [root]
        while root.left is not None:
            self.stack.append(root.left)
            root = root.left

    def next(self) -> int:
        root = self.stack[-1]
        self.stack.pop()
        if root.right is not None:
            right = root.right
            self.stack.append(right)
            while right.left is not None:
                self.stack.append(right.left)
                right = right.left
        return root.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0


if __name__ == '__main__':
    t7 = TreeNode(7)
    t3 = TreeNode(3)
    t15 = TreeNode(15)
    t9 = TreeNode(9)
    t20 = TreeNode(20)
    t7.left = t3
    t7.right = t15
    t15.left = t9
    t15.right = t20
    b = BSTIterator(t7)
    while b.hasNext():
        print(b.next())
