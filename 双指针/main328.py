class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        one = head
        point_one = one
        two = head.next
        point_two = two
        point = two.next
        index = 1
        while point is not None:
            if index % 2 == 1:
                point_one.next = point
                point_one = point
            else:
                point_two.next = point
                point_two = point
            point = point.next
            index += 1
        point_two.next = None
        point_one.next = two
        return one
