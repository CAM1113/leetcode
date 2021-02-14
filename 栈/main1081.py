class Solution:
    def smallestSubsequence(self, s: str) -> str:
        res = []
        for index, c in enumerate(s):
            if c in res:
                continue
            while len(res) > 0 and res[-1] > c and res[-1] in s[index:]:
                res.pop()
            res.append(c)
        return ''.join(res)
