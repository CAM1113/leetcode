# 递归

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_add(l1: ListNode, l2: ListNode):
    if l1.next is None or l2.next is None:
        val = l1.val + l2.val
        add = 0
        if val > 10:
            add = 1
            val = val - 10
        return ListNode(val, None), add
    node, add = get_add(l1.next, l2.next)
    val = l1.val + l2.val + add
    add = 0
    if val > 10:
        add = 1
        val = val - 10
    return ListNode(val, node), add


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        length1 = 0
        while head1 is not None:
            length1 += 1
            head1 = head1.next
        head2 = l2
        length2 = 0
        while head2 is not None:
            length2 += 1
            head2 = head2.next
        if length1 < length2:
            t = l1
            l1 = l2
            l2 = t
        length = abs(length1 - length2)
        while length > 0:
            l2 = ListNode(0, l2)
            length -= 1
        node, add = get_add(l1, l2)
        if add == 1:
            return ListNode(1, node)
        return node

