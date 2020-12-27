class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for idx, c in enumerate(s):
            if dic.get(c) is None:
                dic[c] = [idx, 1]
            else:
                dic[c][1] += 1
        min_idx = 1e10
        for c in dic.values():
            if c[1] == 1 and c[0] < min_idx:
                min_idx = c[0]
        if min_idx == 1e10:
            return -1
        return min_idx
