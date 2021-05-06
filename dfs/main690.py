import collections
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id_importance = collections.defaultdict(int)
        id_nodes = collections.defaultdict(list)

        for e in employees:
            id_importance[e.id] = e.importance
            id_nodes[e.id] = e.subordinates

        stack = [id]
        sums = 0
        while len(stack) != 0:
            c = stack.pop()
            for ss in id_nodes[c]:
                stack.append(ss)
            sums += id_importance[c]
        return sums

