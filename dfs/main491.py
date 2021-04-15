from typing import List


def dfs(nums: List[int], index, result, results):
    if index >= len(nums):
        return

    while index < len(nums):
        if len(result) == 0:
            result.append(nums[index])
            dfs(nums, index + 1, result, results)
            n = result.pop()
            while index < len(nums) and nums[index] == n:
                index += 1

        elif nums[index] >= result[-1]:
            result.append(nums[index])
            results.add(tuple(result[:]))
            dfs(nums, index + 1, result, results)
            n = result.pop()
            while index < len(nums) and nums[index] == n:
                index += 1
        else:
            index += 1


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        results = set()
        dfs(nums, 0, [], results)
        re = [list(t) for t in results]
        return re


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]
    print(Solution().findSubsequences(x))
