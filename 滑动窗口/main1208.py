class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        sums = 0
        start = 0
        length = 0
        while start + length < len(s):
            print(f'{start + length}')
            sums += abs(ord(s[start + length]) - ord(t[start + length]))
            if sums > maxCost:
                sums -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            else:
                length += 1
        return length


if __name__ == '__main__':
    s = "abcd"
    t = "bcdf"
    cost = 3
    print(Solution().equalSubstring(s, t, cost))
