class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(data, index):
    index[0] += 1
    if index[0] > len(data) or data[index[0]] is None:
        return None
    root = TreeNode(data[index[0]])
    root.left = dfs(data, index)
    root.right = dfs(data, index)
    return root


class Codec:

    def serialize(self, root):
        stack = [root]
        vals = []
        while len(stack) != 0:
            r = stack.pop()
            if r is None:
                vals.append(r)
                continue
            vals.append(r.val)
            stack.append(r.right)
            stack.append(r.left)
        return vals

    def deserialize(self, data):
        if data[0] is None:
            return None
        index = [-1]
        return dfs(data, index)


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5
    c = Codec()
    d = c.serialize(t1)
    print(d)
    print(c.deserialize(d))
