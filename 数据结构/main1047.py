class Solution:
    def removeDuplicates(self, S: str) -> str:
        l = []
        for s in S:
            if len(l) == 0 or l[-1] != s:
                l.append(s)
            else:
                l.pop()
        return ''.join(l)
