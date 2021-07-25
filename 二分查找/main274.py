from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        if length == 1:
            if citations[0] >= 1:
                return 1
            else:
                return 0
        citations.sort(reverse=True)
        if citations[0] == 0:
            return 0
        start = 0
        end = length - 1
        while start < end - 1:
            middle = (start + end) // 2
            if citations[middle] >= middle + 1:
                start = middle
            else:
                end = middle
        if citations[end] >= end + 1:
            return end
        return start + 1


if __name__ == '__main__':
    print(Solution().hIndex(citations= [3,0,6,1,5]))
