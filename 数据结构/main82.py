# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None:
            return None
        del_nodes = set()

        p = head
        while p is not None and p.next is not None:
            if p.val == p.next.val:
                del_nodes.add(p.val)
                p.next = p.next.next
            else:
                p = p.next

        temp = ListNode()
        temp.next = head
        p = temp
        while p is not None and p.next is not None:
            if p.next.val in del_nodes:
                p.next = p.next.next
            else:
                p = p.next
        return temp.next


class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None:
            return None


        temp = ListNode()
        temp.next = head
        pre = temp

        while head is not None and head.next is not None:
            if head.val == head.next.val:
                while head.next is not None and head.val == head.next.val:
                    head.next = head.next.next
                pre.next = head.next
                head = pre.next
            else:
                pre = head
                head = head.next
        return temp.next
