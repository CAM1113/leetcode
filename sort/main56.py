# 56. 合并区间
# 给出一个区间的集合，请合并所有重叠的区间。


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return intervals
        intervals = self.sort(intervals, 0, len(intervals) - 1)
        i = 1
        result = [intervals[0]]
        while i < len(intervals):
            if intervals[i][0] <= result[-1][1]:
                right = max(intervals[i][1], result[-1][1])
                result[-1] = [result[-1][0], right]
            else:
                result.append(intervals[i])
            i += 1
        return result

    # 快排
    def sort(self, intervals, start, end):
        if start >= end:
            return intervals
        temp = intervals[start]
        start_index = start
        end_index = end
        temp_index = start_index
        while start_index < end_index:
            if temp_index == start_index:
                if intervals[end_index][0] <= temp[0]:
                    intervals[start_index] = intervals[end_index]
                    temp_index = end_index
                    start_index += 1
                else:
                    end_index -= 1
            else:
                if intervals[start_index][0] < temp[0]:
                    start_index += 1
                else:
                    intervals[end_index] = intervals[start_index]
                    temp_index = start_index
                    end_index -= 1
        intervals[start_index] = temp
        self.sort(intervals, start, start_index - 1)
        self.sort(intervals, start_index + 1, end)
        return intervals


if __name__ == '__main__':
    intervals_ = [[1, 4], [4, 5], [3, 8], [10, 20]]
    re = Solution().merge(intervals_)
    print(re)
