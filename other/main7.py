class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        abs_mask = 1
        max_val = 2147483647
        min_val = -2147483648
        if x == 0:
            return 0
        if x < 0:
            abs_mask = -1
            x = -x
        try:
            while abs(x) > 0:
                num = num * 10 + x % 10
                x = x // 10
        except Exception as e:
            return 0
        if num < min_val or num > max_val:
            return 0
        return num * abs_mask


def main():
    x = -123
    print(Solution().reverse(x))


if __name__ == '__main__':
    main()
