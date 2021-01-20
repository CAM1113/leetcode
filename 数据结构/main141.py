class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1 = head
        p2 = head
        while True:
            if p1 is None or p2 is None:
                return False
            if p1 == p2:
                return True
            p1 = p1.next
            if p2.next is None:
                return False
            p2 = p2.next.next
