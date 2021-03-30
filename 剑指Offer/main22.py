class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p = head
        n = 1
        while p is not None and n < k:
            p = p.next
            n += 1
        if n != k:
            return None
        p2 = head
        while p is not None:
            p = p.next
            p2 = p2.next
        return p2
