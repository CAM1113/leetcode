class Solution:
    def lemonadeChange(self, bills):
        five = 0
        ten = 0
        for m in bills:
            if m == 5:
                five += 1
            if m == 10:
                five -= 1
                ten += 1
                if five < 0:
                    return False
            if m == 20:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
                if five < 0:
                    return False
        return True


def main():
    bills = [5, 5,  20]
    print(Solution().lemonadeChange(bills))


if __name__ == '__main__':
    main()
