# dp两个数组，两个数组互相影响，边界条件很复杂


class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0
        n = len(s)
        if n == 0:
            return 0
        compose_num = [0] * n
        nums = [1] * n
        for i in range(1, n):
            if s[i] == '0':
                if int(s[i - 1]) >= 3 or s[i - 1] == '0':
                    return 0
                if compose_num[i - 1] == 0:
                    nums[i] = nums[i - 1]
                else:
                    nums[i] = nums[i - 1] - compose_num[i - 1]
                compose_num[i] = nums[i]
            else:
                if s[i - 1] == '0':
                    nums[i] = nums[i - 1]
                    compose_num[i] = 0
                    continue
                # 不能组合
                if int(s[i - 1:i + 1]) > 26:
                    nums[i] = nums[i - 1]
                    compose_num[i] = 0
                    continue
                # 可以组合
                if compose_num[i - 1] > 0:
                    nums[i] = (nums[i - 1] - compose_num[i - 1]) * 2 + compose_num[i - 1]
                    compose_num[i] = nums[i - 1] - compose_num[i - 1]
                else:
                    nums[i] = nums[i - 1] * 2
                    compose_num[i] = nums[i - 1]
        return nums[-1]
