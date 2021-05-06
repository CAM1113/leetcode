class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        point1 = headA
        lenA = 0
        point2 = headB
        lenB = 0
        while point1 is not None:
            point1 = point1.next
            lenA += 1
        while point2 is not None:
            point2 = point2.next
            lenB += 1
        more = abs(lenB - lenA)
        more_point = headA
        start_point = headB
        if lenB > lenA:
            more_point = headB
            start_point = headA
        while more > 0:
            more_point = more_point.next
            more -= 1
        while more_point != start_point:
            if more_point is None or start_point is None:
                return None
            more_point = more_point.next
            start_point = start_point.next
        return more_point
