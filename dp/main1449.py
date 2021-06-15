from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        nums = []
        costs = []
        for index, n in enumerate(cost):
            if n in costs:
                n_index = costs.index(n)
                costs.pop(n_index)
                nums.pop(n_index)
            nums.append(index + 1)
            costs.append(n)

        dp = [["" for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        dp[0][0] = " "
        for i in range(1, len(nums) + 1):
            cost_i = costs[i - 1]
            for j in range(target + 1):
                times = 1
                dp[i][j] = dp[i - 1][j]
                while j - times * cost_i >= 0:
                    if len(dp[i - 1][j - times * cost_i]) != 0 and len(dp[i - 1][j - times * cost_i]) + times >= len(
                            dp[i - 1][j]):
                        dp[i][j] = dp[i - 1][j - times * cost_i] + str(nums[i - 1]) * times
                    times += 1
        max_len = 0
        max_num = "0"
        for i in range(len(nums) + 1):
            if len(dp[i][target]) >= max_len:
                max_len = len(dp[i][target])
                max_num = dp[i][target]
        result = max_num[::-1].strip()
        if len(result) == 0:
            return ""
        return result


if __name__ == '__main__':
    x = [2, 4, 6, 2, 4, 6, 4, 4, 4]
    t = 5
    print(Solution().largestNumber(x, t))
