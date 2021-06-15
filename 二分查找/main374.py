def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        start = 0
        end = n + 1
        while start - 1 < end:
            middle = (start + end) // 2
            num = guess(middle)
            if num < 0:
                end = middle
                continue
            if num == 0:
                return middle
            if num > 0:
                start = middle
        return start
