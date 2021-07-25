from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal == 1:
            return sum(nums)
        pri_sum = [0]
        for i in nums:
            pri_sum.append(pri_sum[-1] + i)
        if pri_sum[-1] == 0:
            if goal == 0:
                return (len(nums) + 1) * len(nums) // 2

        start = 0
        end = 1
        result = 0
        while end < len(pri_sum):
            sub = pri_sum[end] - pri_sum[start]
            if sub == goal:
                while end < len(pri_sum) and pri_sum[end] - pri_sum[start] == goal:
                    result += 1
                    end += 1
                end -= 1
                while start < end and pri_sum[end] - pri_sum[start] == goal:
                    result += 1
                    start += 1

                end = start + 1
                continue

            if sub > goal:
                start += 1
                if end == start:
                    end += 1
                continue
            if sub < go\
                    al:
                end += 1
                continue
        return result


if __name__ == '__main__':
    print(Solution().numSubarraysWithSum(nums=[0, 0, 0, 0, 0, 0, 1, 0, 0, 0], goal=0))
