def is_ok(c):
    return 'a' <= c <= 'z' or '0' <= c <= '9'


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.strip()
        if len(s) == 0:
            return True
        start = 0
        end = len(s) - 1
        while start != end:
            while start < len(s) and not is_ok(s[start]):
                start += 1
            while end >= 0 and not is_ok(s[end]):
                end -= 1
            if start > end:
                return True
            if s[start] == s[end]:
                start += 1
                end -= 1
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    x = "race a car"
    print(Solution().isPalindrome(x))
