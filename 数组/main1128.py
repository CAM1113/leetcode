from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num_dic = {}
        for c in dominoes:
            c.sort()
            key = c[0] * 10 + c[1]
            if num_dic.get(key) is None:
                num_dic[key] = 1
            else:
                num_dic[key] += 1
        total = 0
        for k in num_dic.keys():
            total += (num_dic[k] - 1) * num_dic[k] / 2
        return total
