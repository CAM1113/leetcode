class Solution:
    def largeGroupPositions(self, s: str):
        res = []
        if len(s) < 3:
            return res
        start = 0
        end = 1
        while end < len(s):
            if s[end] == s[start]:
                end += 1
            else:
                if end - start >= 3:
                    res.append([start, end - 1])
                start = end
                end += 1
        end -= 1
        if end - start >= 3:
            res.append([start, end])
        return res
