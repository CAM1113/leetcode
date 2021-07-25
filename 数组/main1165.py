import collections


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        positions = collections.defaultdict(lambda: 0)
        for index, k in enumerate(keyboard):
            positions[k] = index
        index = 1
        ll = 0
        while index < len(word):
            ll += abs(positions[index] - positions[index - 1])
            index += 1
        return ll
