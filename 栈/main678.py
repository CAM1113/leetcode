import collections


class Solution:
    def checkValidString(self, s: str) -> bool:
        left = collections.deque()
        start = collections.deque()
        for index, c in enumerate(s):
            if c == "(":
                left.append(index)
            elif c == "*":
                start.append(index)
            else:
                if len(left) > 0:
                    left.pop()
                elif len(start) > 0:
                    start.pop()
                else:
                    return False
        while len(left) > 0 and len(start) > 0:
            if left[-1] < start[-1]:
                left.pop()
                start.pop()
            else:
                return False
        return len(left) == 0
