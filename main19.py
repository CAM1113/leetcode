from Utils import ListNode


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
