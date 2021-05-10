from typing import List


def is_ok(bloomDay: List[int], m: int, k: int, length: int):
    k_sums = 0
    for i in bloomDay:
        if i <= length:
            k_sums += 1
            if k_sums == k:
                k_sums = 0
                m -= 1
                if m == 0:
                    return True
        else:
            k_sums = 0
    return False


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        start = 10e9
        end = 0
        if len(bloomDay) < m * k:
            return -1
        for b in bloomDay:
            if b < start:
                start = b
            if b > end:
                end = b
        if is_ok(bloomDay, m, k, start):
            return start
        while start < end - 1:
            middle = (start + end) // 2
            if is_ok(bloomDay, m, k, middle):
                end = middle
            else:
                start = middle
        return is_ok(bloomDay, m, k, start)


if __name__ == '__main__':
    bloomDay = [7, 7, 7, 7, 12, 7, 7]

    m = 2
    k = 3
    print(Solution().minDays(bloomDay, m, k))
