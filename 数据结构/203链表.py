# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int):
        while head is not None:
            if head.val == val:
                head = head.next
            else:
                break
        if head is None:
            return None
        pre = head
        ne = head.next
        while ne is not None:
            if ne.val == val:
                pre.next = ne.next
                ne = ne.next
            else:
                pre = ne
                ne = ne.next
        return head
