class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_list(lists):
    if len(lists) == 1:
        return lists[0]
    if len(lists) == 2:
        head = ListNode()
        p = head
        while len(lists) > 1:
            idx = 0
            temp = lists[0]
            temp_idx = 0
            while idx < len(lists):
                if lists[idx] is None:
                    lists.pop(idx)
                    continue
                if temp is None or lists[idx].val < temp.val:
                    temp = lists[idx]
                    temp_idx = idx
                idx += 1
            if temp is None:
                return head.next
            p.next = temp
            p = temp
            lists[temp_idx] = temp.next
        p.next = lists[0]
        return head.next
    list1 = merge_list(lists[0:len(lists) // 2])
    list2 = merge_list(lists[len(lists) // 2:len(lists)])
    return merge_list([list1, list2])


class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        return merge_list(lists)
