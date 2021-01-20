class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def dfs(current: ListNode, pre: ListNode):
    if current is None:
        return pre
    ret = dfs(current.next, current)
    current.next = pre
    return ret


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return dfs(head, None)


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    head = Solution().reverseList(l1)
    while head is not None:
        print(head.val)
        head = head.next
