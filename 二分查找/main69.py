class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        start = 0
        end = x
        while start < end - 1:
            middle = (start + end) // 2
            tw = middle ** 2
            if tw == x:
                return middle
            if tw < x:
                start = middle
            elif tw > x:
                end = middle
        return start


if __name__ == '__main__':
    x = 8
    print(Solution().mySqrt(x))
