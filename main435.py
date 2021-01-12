from typing import List


def sort_key(a):
    return a[1]


def is_cross(a, b):
    if a[0] <= b[0] < a[1]:
        return True
    if b[0] <= a[0] <= b[1]:
        return True
    return False


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=sort_key)
        new_intervals = [intervals[0]]
        index = 1
        while index < len(intervals):
            if not is_cross(new_intervals[-1], intervals[index]):
                new_intervals.append(intervals[index])
            index += 1
        return len(intervals) - len(new_intervals)


if __name__ == '__main__':
    x = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(Solution().eraseOverlapIntervals(x))
