# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = 0
        point = head
        tail = point
        while point is not None:
            length += 1
            tail = point
            point = point.next

        off_set = k % length

        off_set = length - off_set
        point = head
        current_point = 0
        while point is not None:
            current_point += 1
            if current_point == off_set:
                break
            point = point.next
        tail.next = point
        point.next = None
