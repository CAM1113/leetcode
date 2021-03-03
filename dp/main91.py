def is_can_compose(s):
    if s.startswith('0'):
        return False
    if int(s) <= 26:
        return True
    return False


class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0
        n = len(s)
        if n == 0:
            return 0
        is_compose = [0] * n
        nums = [1] * n
        for i in range(1, n):
            if s[i] == '0':
                if int(s[i - 1]) >= 3 or s[i - 1] == '0':
                    return 0
                if is_compose[i - 1] == 0:
                    nums[i] = nums[i - 1]
                    is_compose[i] = nums[i]
                else:
                    nums[i] = nums[i - 1] - is_compose[i - 1]
                    is_compose[i] = nums[i]
            else:
                if s[i - 1] == '0':
                    nums[i] = nums[i - 1]
                    is_compose[i] = 0
                    continue

                if is_compose[i - 1] > 0:
                    if is_can_compose(s[i - 1:i + 1]):
                        nums[i] = (nums[i - 1] - is_compose[i - 1]) * 2 + is_compose[i - 1]
                        is_compose[i] = nums[i - 1] - is_compose[i - 1]
                    else:
                        nums[i] = nums[i - 1]
                        is_compose[i] = 0

                else:
                    if is_can_compose(s[i - 1:i + 1]):
                        nums[i] = nums[i - 1] * 2
                        is_compose[i] = nums[i - 1]
                    else:
                        nums[i] = nums[i - 1]
                        is_compose[i] = 0

        return nums[-1]


if __name__ == '__main__':
    x = "111111111111111111111111111111111111111111111"

    print(Solution().numDecodings(x))
