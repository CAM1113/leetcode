from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = []
        index = 0
        for r in mat:
            strength.append((sum(r), index))
            index += 1
        strength.sort(key=lambda x: x[0])
        result = [i[1] for i in strength]
        return result[:k]
