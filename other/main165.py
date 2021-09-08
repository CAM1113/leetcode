def get_num(s):
    num = 0
    zero = ord('0')
    for c in s:
        num = num * 10 + (ord(c) - zero)
    return num


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        index = 0
        while index < len(v1) and index < len(v2):
            n1 = get_num(v1[index])
            n2 = get_num(v2[index])
            if n1 > n2:
                return 1
            if n1 < n2:
                return -1
            index += 1
        longer = v1
        if len(v1) < len(v2):
            longer = v2
        while index < len(longer):
            n = get_num(longer[index])
            if n > 0:
                return 1
            index += 1
        return 0
