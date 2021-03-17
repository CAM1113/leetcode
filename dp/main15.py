class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        last_position = []
        for i in range(len(s)):
            if s[i] == t[0]:
                last_position.append((i, 1))

        for i in range(1, len(t)):
            last = []
            if len(last_position) == 0:
                return 0
            for j in range(last_position[0][0], len(s)):
                if s[j] == t[i]:
                    numc = 0
                    for p in last_position:
                        if p[0] >= j:
                            break
                        numc += p[1]
                    last.append((j, numc))
            last_position = last
        return sum([n[1] for n in last_position])




if __name__ == '__main__':
    s = "bbaabacbbc"
    t = "cbacccb"
    print(Solution().numDistinct(s, t))
