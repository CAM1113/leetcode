class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = {}
        for c in s:
            if s_dict.get(c) is None:
                s_dict[c] = 1
            else:
                s_dict[c] = s_dict[c] + 1

        for c in t:
            if s_dict.get(c) is None or s_dict[c] == 0:
                return c
            else:
                s_dict[c] = s_dict[c] - 1


def main():
    s = "abcd"
    t = "abcde"
    print(Solution().findTheDifference(s, t))


if __name__ == '__main__':
    main()
