from typing import List


# 递归回溯+剪枝去重

def dfs(nums, index, result, results):
    if index == len(nums):
        return

    result.append(nums[index])
    results.append(result[:])
    dfs(nums, index + 1, result, results)

    result.pop()
    while index + 1 < len(nums) and nums[index] == nums[index + 1]:
        index += 1
    dfs(nums, index + 1, result, results)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        results = [[]]
        dfs(nums, 0, result, results)
        return results


def main():
    nums = [1, 2, 2, 3]
    print(Solution().subsetsWithDup(nums))


if __name__ == '__main__':
    main()
