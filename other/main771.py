from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = Counter(stones)
        result = 0
        for c in jewels:
            if c in stones.keys():
                result += stones[c]
        return result
