from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = [n for _ in range(n)]
        index = 0
        steps[0] = 0
        min_step = 0
        while index < len(nums):
            if min_step > index + nums[index]:
                index += 1
                continue
            for i in range(min_step + 1,index + nums[index] + 1):
                if i >= n:
                    return steps[-1]
                if steps[i] > steps[index] + 1:
                    steps[i] = steps[index] + 1
            min_step = index + nums[index]
            index += 1
            if min_step >= n:
                break
        return steps[-1]


if __name__ == '__main__':
    s = [2, 3, 1, 1, 4]
    print(Solution().jump(s))
