
# 链表经典题，思路最重要

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# 暴力
class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        p1 = head
        head2 = Node(p1.val)
        p2 = head2
        while p1 is not None:
            p1 = p1.next
            new_node = Node(p1.val)
            p2.next = new_node
            p2 = new_node

        p1 = head
        p2 = head2
        while p1.next is not None:
            if p1.random is None:
                p2.random = None
            else:
                p_temp1 = head
                p_temp2 = head2
                while p1.random != p_temp1:
                    p_temp1 = p_temp1.next
                    p_temp2 = p_temp2.next
                p2.random = p_temp2
            p1 = p1.next
            p2 = p2.next
        return head2


# 链表
class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        p1 = head
        while p1 is not None:
            new_node = Node(p1.val)
            new_node.next = p1.next
            p1.next = new_node
            p1 = p1.next.next

        p1 = head
        while p1 is not None:
            if p1.random is None:
                p1.next.random = None
            else:
                p1.next.random = p1.random.next
            p1 = p1.next.next

        head2 = head.next
        p2 = head2
        while p2.next is not None:
            p2.next = p2.next.next
            p2 = p2.next

        return head2


# 哈希
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        new_node_dic = {}
        p1 = head
        while p1 is not None:
            new_node = Node(p1.val)
            new_node_dic[p1] = new_node
            p1 = p1.next

        p1 = head
        while p1 is not None:
            new_node_dic[p1].next = new_node_dic[p1.next]
            if p1.random is None:
                new_node_dic[p1].random = None
            else:
                new_node_dic[p1].random = new_node_dic[p1.random]
            p1 = p1.next

        return new_node_dic[head]
