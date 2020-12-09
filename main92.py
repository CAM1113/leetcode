# 92. 反转链表 II
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        m = m - 1
        n = n - 1
        if m == n:
            return head
        index_next = head
        index_num = 0
        start = None
        start_1 = None
        end = None
        last = None
        if m == 0:
            start_1 = head
        while index_next is not None:
            if index_num == m - 1:
                start = index_next
                start_1 = start.next
                last = index_next
                index_next = index_next.next
            elif index_num == n + 1:
                end = index_next
                break
            elif m <= index_num <= n:
                temp = index_next
                index_next = index_next.next
                temp.next = last
                last = temp
                if m == 0:
                    head = last
            else:
                index_next = index_next.next
            index_num += 1

        start_1.next = end
        if start is not None:
            start.next = last
        return head


if __name__ == '__main__':
    head = ListNode(1)
    next = head
    for i in range(2, 6):
        node = ListNode(i)
        next.next = node
        next = node
    nest = head
    while nest is not None:
        print(nest.val)
        nest = nest.next

    s = Solution()
    head = s.reverseBetween(head, 3, 4)


