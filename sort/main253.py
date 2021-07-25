from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        ranges = [intervals[0]]
        for i in range(1, len(intervals)):
            n = intervals[i]
            is_ok = False
            for index, inter in enumerate(ranges):
                if n[0] >= inter[1]:
                    ranges[index] = n
                    is_ok = True
                    break
            if not is_ok:
                ranges.append(n)
        return len(ranges)


if __name__ == '__main__':
    print(Solution().minMeetingRooms(intervals=[[1,5],[8,9],[8,9]]))
