class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = []
        for idx, c in enumerate(s):
            if c in result:
                continue
            while len(result) > 0 and c < result[-1] and result[-1] in s[idx:]:
                result.pop()
            result.append(c)
        r = ''.join(result)
        return r


def main():
    s = "cbacdcbc"
    print(Solution().removeDuplicateLetters(s))


if __name__ == '__main__':
    main()
