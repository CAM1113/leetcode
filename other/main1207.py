from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for n in arr:
            if dic.get(n) is None:
                dic[n] = 1
            else:
                dic[n] += 1
        v_dic = set(dic.values())

        return len(v_dic) == len(dic.keys())