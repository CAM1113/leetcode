from random import random


class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        t = 0
        for a in w:
            t += a
            self.prefix.append(t)

    def pickIndex(self) -> int:
        x = random.uniform(0, self.prefix[-1])
        if x < self.prefix[0]:
            return 0
        start = 0
        end = len(self.prefix) - 1
        while start < end - 1:
            middle = (start + end) // 2
            if self.prefix[middle] < x:
                start = middle
            else:
                end = middle
        return end
