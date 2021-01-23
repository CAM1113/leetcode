class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def dfs(node, n_current, val_set):
    if node.val in val_set.keys():
        return
    val_set[node.val] = n_current
    for c in node.neighbors:
        if val_set.get(c.val) is not None:
            n_current.neighbors.append(val_set[c.val])
        else:
            n = Node(c.val)
            dfs(c, n, val_set)
            n_current.neighbors.append(n)


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        n = Node(node.val)
        val_set = {}
        dfs(node, n, val_set)
        return n


def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    print(Solution().cloneGraph(n1))


if __name__ == '__main__':
    main()
