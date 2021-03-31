from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target < 3:
            return [[]]
        start = 1
        end = 2
        final = target // 2 + 1
        sums = 3
        window = [1, 2]
        result = []
        while start < end <= final:
            while sums < target:
                end += 1
                window.append(end)
                sums += end
            if sums == target:
                result.append(window[:])
                window.pop(0)
                sums -= start
                start += 1
                continue
            while sums > target:
                window.pop(0)
                sums -= start
                start += 1
            if sums == target:
                result.append(window[:])
                window.pop(0)
                sums -= start
                start += 1
                continue
        return result


if __name__ == '__main__':
    t = 15
    print(Solution().findContinuousSequence(t))
