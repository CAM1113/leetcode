class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next is None:
            return True
        slow = head
        fast = head.next
        if fast.next is None:
            if fast.val == slow.val:
                return True
            else:
                return False
        fast = fast.next
        pHead = None
        while fast is not None:
            if fast.next is None or fast.next.next is None:
                pHead = slow.next.next
                break
            fast = fast.next.next
            slow = slow.next
        reverseHead = ListNode(0)
        while pHead is not None:
            pHeadNext = pHead.next
            pHead.next = reverseHead.next
            reverseHead.next = pHead
            pHead = pHeadNext
        reverseHead = reverseHead.next
        while reverseHead is not None:
            if head.val == reverseHead.val:
                reverseHead = reverseHead.next
                head = head.next
            else:
                return False
        return True

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(2)
    n4 = ListNode(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    print(Solution().isPalindrome(n1))