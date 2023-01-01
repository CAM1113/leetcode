class Solution:
    def repeatedCharacter(self, s: str) -> str:
        sets = set()
        for c in s:
            if c in sets:
                return c
            else:
                sets.add(c)