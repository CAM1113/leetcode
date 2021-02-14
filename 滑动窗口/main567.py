def judge(cnt1, cnt2):
    if len(cnt1.keys()) != len(cnt2.keys()):
        return False
    for c in cnt1.keys():
        if c not in cnt2.keys():
            return False
        if cnt1[c] != cnt2[c]:
            return False
    return True


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cnt1 = {}
        for c in s1:
            if c in cnt1.keys():
                cnt1[c] += 1
            else:
                cnt1[c] = 1
        start = 0
        length = len(s1)
        cnt2 = {}
        ss = s2[:length]
        for c in ss:
            if c in cnt2.keys():
                cnt2[c] += 1
            else:
                cnt2[c] = 1

        while start + length < len(s2):
            if judge(cnt1, cnt2):
                return True
            if s2[start + length] in cnt2.keys():
                cnt2[s2[start + length]] += 1
            else:
                cnt2[s2[start + length]] = 1

            cnt2[s2[start]] -= 1
            if cnt2[s2[start]] == 0:
                del cnt2[s2[start]]
            start += 1

        return judge(cnt1, cnt2)


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1, s2))
