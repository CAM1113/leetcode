# 57. 插入区间
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

def adjust(intervals, start):
    start_inter_end = intervals[start][1]
    next_index = start + 1
    while True:
        if next_index >= len(intervals):
            break
        if start_inter_end > intervals[next_index][1]:
            intervals.pop(next_index)
            continue
        if start_inter_end >= intervals[next_index][0]:
            intervals[start][1] = intervals[next_index][1]
            intervals.pop(next_index)
            return intervals

        if start_inter_end < intervals[next_index][0]:
            break

    return intervals


class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        start = 0
        while True:
            if newInterval[0] <= intervals[start][1]:
                break
            start += 1
        if newInterval[0] <= intervals[start][0] and newInterval[1] < intervals[start][0]:
            intervals.insert(start,newInterval)
            return intervals

        if newInterval[0] <= intervals[start][0] and newInterval[1] <= intervals[start][1]:
            intervals[start][0] = newInterval[0]
            return intervals

        if newInterval[0] <= intervals[start][0] and newInterval[1] > intervals[start][1]:
            intervals[start][0] = newInterval[0]
            intervals[start][1] = newInterval[1]
            return adjust(intervals, start)

        if newInterval[0] > intervals[start][0] and newInterval[1] < intervals[start][1]:
            return intervals

        else:
            intervals[start][1] = newInterval[1]
            return adjust(intervals, start)


def main():
    intervals = [[3,8],[9,11]]

    newInterval = [3,7]
    print(Solution().insert(intervals, newInterval))


if __name__ == '__main__':
    main()
