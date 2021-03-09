class Solution:
    def minOperations(self, s: str) -> int:
        change0 = 0
        change1 = 0
        is_zero = True
        for c in s:
            if c == '0':
                if is_zero:
                    change1 += 1
                else:
                    change0 += 1
            if c == '1':
                if is_zero:
                    change0 += 1
                else:
                    change1 += 1
            is_zero = not is_zero
        return min(change0, change1)


if __name__ == '__main__':
    x = "1111"
    print(Solution().minOperations(x))
