class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split(" ")
        pattern = list(pattern)
        kv = {}
        if len(pattern) != len(ss):
            return False
        for p, s in zip(pattern, ss):
            keys = kv.keys()
            vals = kv.values()
            if p in keys:
                if s != kv[p]:
                    return False
                continue
            if s in vals:
                return False
            kv[p] = s
        return True


def main():
    pattern = "abba"
    s = "dog dd cat dog"
    print(Solution().wordPattern(pattern, s))


if __name__ == '__main__':
    main()
