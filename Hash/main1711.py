import collections
from itertools import count
from typing import List


def is_used(used, i, j):
    mi = min(i, j)
    mx = max(i, j)
    h = mx * 10 ** 10 + mi
    if h not in used:
        used.add(h)
        return False
    return True


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnt = collections.defaultdict(lambda: 0)
        for d in deliciousness:
            cnt[d] += 1
        two = set()
        t = 1
        two.add(t)
        for i in range(22):
            t *= 2
            two.add(t)
        keys = cnt.keys()
        result = 0
        mod = 10 ** 9 + 7
        used = set()
        for i in keys:
            for jj in two:
                j = jj - i
                if j < 0 or j not in keys:
                    continue

                if is_used(used, i, j):
                    continue

                if (i + j) in two:
                    if i == j:
                        n = cnt[i]
                        result += (n - 1) * n // 2
                        result %= mod
                    else:
                        n1 = cnt[i]
                        n2 = cnt[j]
                        result += n1 * n2
                        result %= mod
        return result


if __name__ == '__main__':
    print(Solution().countPairs(deliciousness=[1, 1, 1, 3, 3, 3, 7]))
