class Solution:
    def isUnique(self, astr: str) -> bool:
        s = set()
        for c in astr:
            if c in s:
                return False
            s.add(c)
        return True
