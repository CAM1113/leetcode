import collections
from typing import List


def get_content(s: str):
    d = collections.defaultdict(int)
    for c in s:
        d[c] += 1
    res = ""
    keys = list(d.keys())
    keys.sort()
    for k in keys:
        res += f"{k}:{d[k]}"
    return res


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for s in strs:
            content = get_content(s)
            result[content].append(s)
        return list(result.values())
