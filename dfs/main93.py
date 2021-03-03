from typing import List


def is_ok(result: List[str]):
    if len(result) != 4:
        return False
    for r in result:
        n = int(r)
        if r.startswith('0') and n != 0:
            return False
        if n > 255:
            return False
    return True


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        for p1 in range(1, 4):
            if s[:p1].startswith('00'):
                break
            for p2 in range(p1 + 1, p1 + 4):
                if p2 > len(s):
                    break
                if s[p1:p2].startswith('00'):
                    break
                for p3 in range(p2 + 1, p2 + 4):
                    if p3 > len(s) - 1:
                        break
                    if s[p2:p3].startswith('00'):
                        break
                    if len(s) - p3 > 3:
                        continue
                    if s[p3:].startswith('00'):
                        continue
                    result = [s[:p1], s[p1:p2], s[p2:p3], s[p3:]]
                    if is_ok(result):
                        results.append(".".join(result))
        return results


if __name__ == '__main__':
    s =  "25525511135"
    print(Solution().restoreIpAddresses(s))
