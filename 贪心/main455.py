class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        g = g[::-1]
        s = s[::-1]
        n = 0
        index = 0
        for food in s:
            while index < len(g) and food < g[index]:
                index += 1
            if index >= len(g):
                break
            n += 1
            index += 1
        return n
