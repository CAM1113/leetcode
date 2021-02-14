from typing import List


def dfs(nums, is_used, result, results):
    if len(result) == len(nums):
        results.append(result[:])
        return
    index = 0
    while index < len(nums):
        if is_used[index]:
            index += 1
            continue
        result.append(nums[index])
        is_used[index] = True
        dfs(nums, is_used, result, results)
        temp = nums[index]
        is_used[index] = False
        result.pop()
        while index < len(nums) and nums[index] == temp:
            index += 1


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        is_used = [False for _ in nums]
        result = []
        results = []
        dfs(nums, is_used, result, results)
        return results


if __name__ == '__main__':
    x = [1,1,2]
    print(Solution().permuteUnique(x))
