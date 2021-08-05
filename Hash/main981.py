import collections
from typing import List, Tuple


def binary_search(lis: List[Tuple], time_stamp: int):
    if len(lis) == 0 or lis[0][1] > time_stamp:
        return ""
    if lis[-1][1] <= time_stamp:
        return lis[-1][0]
    if lis[0][1] == time_stamp:
        return lis[0][0]

    start = 0
    end = len(lis) - 1
    while start < end - 1:
        middle = (start + end) // 2
        if lis[middle][1] == time_stamp:
            return lis[middle][0]
        if lis[middle][1] < time_stamp:
            start = middle
        else:
            end = middle
    return lis[start][0]


class TimeMap:

    def __init__(self):
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lis = self.dic[key]
        return binary_search(lis, timestamp)
