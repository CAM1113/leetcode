class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        p = ListNode(0)
        p.next = head
        head = p
        fast = head.next.next
        slow = head.next

        while fast is not None and fast != slow:
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            slow = slow.next

        if fast is None:
            return None

        p = head
        while p != fast:
            p = p.next
            fast = fast.next
        return p


if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p2

    print(Solution().detectCycle(p1).val)
