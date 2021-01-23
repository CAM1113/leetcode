class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        result = 0
        for index, c in enumerate(s):
            if c == 'I':
                if index + 1 < n and (s[index + 1] == 'V' or s[index + 1] == 'X'):
                    result += -1
                else:
                    result += 1
            elif c == 'V':
                result += 5
            elif c == 'X':
                if index + 1 < n and (s[index + 1] == 'L' or s[index + 1] == 'C'):
                    result += -10
                else:
                    result += 10
            elif c == 'L':
                result += 50
            elif c == 'C':
                if index + 1 < n and (s[index + 1] == 'D' or s[index + 1] == 'M'):
                    result += -100
                else:
                    result += 100
            elif c == 'D':
                result += 500
            else:
                result += 1000
        return result


if __name__ == '__main__':
    ss = "MCMXCIV"
    print(Solution().romanToInt(ss))
