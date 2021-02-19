class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        minus = 1
        total = 0
        mins = - 2 ** 31
        maxs = 2 ** 31 - 1
        if s[0] == '-':
            minus = -1
            s = s[1:]
        elif s[0] == '+':
            minus = 1
            s = s[1:]
        index = 0
        while index < len(s):
            if '0' <= s[index] <= '9':
                total *= 10
                total += int(s[index])
                index += 1
            else:
                break
            if total * minus < mins:
                return mins
            if total * minus > maxs:
                return maxs
        return minus * total


if __name__ == '__main__':
    ss = "words and 987"
    print(Solution().myAtoi(ss))
