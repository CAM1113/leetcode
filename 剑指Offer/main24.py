class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def dfs(head: ListNode):
    if head.next is None:
        return head, head
    x, tail = dfs(head.next)
    x.next = head
    head.next = None
    return head, tail


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        _, tail = dfs(head)
        return tail


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    l3.next = None
    print(Solution().reverseList(l1))
