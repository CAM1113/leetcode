class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        pre = temp
        p = head
        while p is not None:
            if p.val == val:
                pre.next = p.next
                p.next = None
                break
            else:
                pre = p
                p = p.next
        return temp.next
