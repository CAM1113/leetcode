import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        head = ListNode(val=sys.maxsize, next=head)
        current_point = head.next
        pre_point = head

        while current_point is not None:
            if current_point.val == pre_point.val:
                current_point = current_point.next
                pre_point.next = pre_point.next.next
            else:
                pre_point = current_point
                current_point = current_point.next
        return head.next
