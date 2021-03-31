import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        order_dict = collections.OrderedDict()
        for c in s:
            if c in order_dict.keys():
                order_dict[c] += 1
            else:
                order_dict[c] = 1
        for c in order_dict.keys():
            if order_dict[c] == 1:
                return c
        return " "