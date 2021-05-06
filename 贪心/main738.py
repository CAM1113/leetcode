class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        lis_digits = [N % 10]
        while N > 0:
            digit = N % 10
            if digit > lis_digits[0]:
                for index in range(len(lis_digits)):
                    if lis_digits[index] == 9:
                        break
                    lis_digits[index] = 9
                lis_digits.insert(0, digit - 1)
            else:
                lis_digits.insert(0, digit)
            N = N // 10
        lis_digits.pop(-1)
        num = 0
        for i in lis_digits:
            num = num * 10 + i
        return num


def main():
    N = 1234
    print(Solution().monotoneIncreasingDigits(N))


if __name__ == '__main__':
    main()
