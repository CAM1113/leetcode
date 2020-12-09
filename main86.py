# 86. 分隔链表
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#

# Definition for singly-linked list.
from Utils import ListNode, print_list


class Solution(object):
    def partition(self, head, x):
        smaller = ListNode(0)
        larger = ListNode(0)
        next_node = head
        small_next = smaller
        larger_next = larger
        while next_node is not None:
            if next_node.val < x:
                small_next.next = next_node
                small_next = small_next.next
            else:
                larger_next.next = next_node
                larger_next = larger_next.next
            next_node = next_node.next
        small_next.next = None
        larger_next.next = None
        small_next.next = larger.next
        return smaller.next


if __name__ == '__main__':
    head = ListNode(1).append(4).append(3).append(2).append(5).append(2)
    head = Solution().partition(head, 3)
    print_list(head)
