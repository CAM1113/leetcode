import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = collections.defaultdict(int)
        for c in s:
            cnt[c] += 1

        cnt_list = [(c, n) for c, n in cnt.items()]
        cnt_list.sort(key=lambda x: x[1],reverse=True)
        result = [c * n for c,n in cnt_list]
        return ''.join(result)

