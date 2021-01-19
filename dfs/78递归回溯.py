def dfs(nums, results, result, start_index):
    results.append(result[:])
    if start_index == len(nums):
        return
    for i in range(start_index,len(nums)):
        result.append(nums[i])
        dfs(nums, results, result, i + 1)
        result.pop()


class Solution:
    def subsets(self, nums):
        result = []
        results = []
        start_index = 0
        dfs(nums, results, result, start_index)
        return results


def main():
    nums = [1, 2, 3]
    print(Solution().subsets(nums))


if __name__ == '__main__':
    main()