class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return False
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) < len(t):
            s, t = t, s
        if len(s) == 1 and len(t) == 0:
            return True
        is_change = False
        inds = 0
        indt = 0
        while inds < len(s) and indt < len(t):
            if s[inds] == t[indt]:
                inds += 1
                indt += 1
                continue
            else:
                if is_change:
                    return False
                is_change = True
                if len(s) != len(t):
                    inds += 1
                else:
                    inds += 1
                    indt += 1
        return is_change or len(s) > len(t)


if __name__ == '__main__':
    s = "cab"
    t = "ca"
    print(Solution().isOneEditDistance(s, t))
