import collections


def is_ok(l1, l2):
    for i1, i2 in zip(l1, l2):
        if i1 > i2:
            return False
    return True


class Solution:
    def balancedString(self, s: str) -> int:
        cnt = [0, 0, 0, 0]
        index_map = {"Q": 0, "W": 1, "E": 2, "R": 3}
        for c in s:
            cnt[index_map[c]] += 1

        need_len = len(s) // 4
        need_cnt = [max(0, i - need_len) for i in cnt]
        min_len = sum(need_cnt)
        while True:
            current_cnt = [0, 0, 0, 0]
            start = 0
            end = min_len
            for i in range(min_len):
                c = s[i]
                current_cnt[index_map[c]] += 1
            if is_ok(need_cnt, current_cnt):
                return min_len
            while end < len(s):
                current_cnt[index_map[s[start]]] -= 1
                start += 1
                current_cnt[index_map[s[end]]] += 1
                end += 1
                if is_ok(need_cnt, current_cnt):
                    return min_len
            min_len += 1


if __name__ == '__main__':
    s = "WQWRQQQW"
    print(Solution().balancedString(s))
