from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        sums_day = [0]
        s = 0
        for c in candiesCount:
            s += c
            sums_day.append(s)
        result = []
        for q in queries:
            type_, day_, cap_ = q[0], q[1], q[2]
            if sums_day[type_] // cap_ <= day_ < sums_day[type_+1]:
                result.append(True)
            else:
                result.append(False)
        return result


if __name__ == '__main__':
    candiesCount = [5,2,6,4,1]
    queries =  [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
    print(Solution().canEat(candiesCount, queries))
