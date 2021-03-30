class Solution:
    def isNumber(self, s: str) -> bool:
        start = 0
        if s[0] == '+' or s[0] == '-':
            start = 1
        i = start
        while i < len(s):
            if '0' < s[i] < '9':
                continue
            if s[]
