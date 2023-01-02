import collections
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = [i for  i in arr]
        sorted_arr.sort()
        cnt_sort = 0
        sort_map = collections.defaultdict(lambda : 0)
        cnt_ori = 0
        ori_map = collections.defaultdict(lambda : 0)
        blocls = 0
        for index in range(len(arr)):
            value1 = sorted_arr[index]
            value2 = arr[index]
            if value2 == value1:
                if cnt_ori == cnt_sort == 0:
                    blocls += 1
                continue
            if ori_map[value1] > 0:
                ori_map[value1] -= 1
                cnt_ori -= 1
            else:
                sort_map[value1] += 1
                cnt_sort += 1
            if sort_map[value2] > 0:
                sort_map[value2] -= 1
                cnt_sort -= 1
            else:
                ori_map[value2] += 1
                cnt_ori += 1
            if cnt_ori == cnt_sort == 0:
                blocls += 1
        return blocls

