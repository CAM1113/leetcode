import collections
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        steps_dict = collections.defaultdict(set)
        steps_dict[0].add(1)
        for s in stones:
            for step in steps_dict[s]:
                if s + step == stones[-1]:
                    return True
                steps_dict[s + step].add(step)
                steps_dict[s + step].add(step + 1)
                steps_dict[s + step].add(max(step - 1, 0))
        return False
