from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        start = [0, 0]
        length = abs(start[0] - target[0]) + abs(start[1] - target[1])
        for g in ghosts:
            l = abs(g[0] - target[0]) + abs(g[1] - target[1])
            if l < length:
                return False
        return True
