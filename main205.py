class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        idx = 0

        for c1, c2 in zip(s, t):
            if c1 in dic1 and c2 in dic2 and dic1[c1] == dic2[c2]:
                continue
            if c1 not in dic1 and c2 not in dic2:
                dic1[c1] = idx
                dic2[c2] = idx
                idx += 1
                continue
            return False
        return True
