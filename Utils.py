class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def append(self, x):
        l = self
        while l.next is not None:
            l = l.next
        l.next = ListNode(x)
        return self


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_list(lis):
    nest = lis
    while nest is not None:
        print(nest.val)
        nest = nest.next


# 中序打印树
def print_tree(node):
    if node is None:
        return
    print_tree(node.left)
    print(node.val)
    print_tree(node.right)


