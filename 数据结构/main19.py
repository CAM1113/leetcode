class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        nodes = []
        while p is not None:
            nodes.append(p)
            p = p.next
        if len(nodes) == 1:
            return None
        index = len(nodes) - n

        if index == 0:
            return nodes[1]
        nodes[index - 1].next = nodes[index].next
        return nodes[0]
