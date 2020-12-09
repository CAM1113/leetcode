import copy
def dfs(is_used, nums, result, results):
    if len(result) == len(nums):
        results.append(result[:])
        return
    for i in range(len(nums)):
        if is_used[i] != 1:
            is_used[i] = 1
            result.append(nums[i])
            dfs(is_used,nums,result,results)
            is_used[i] = 0
            result.pop(-1)


class Solution:
    def permute(self, nums):
        is_used = [0 for _ in range(len(nums))]
        results = []
        result = []
        dfs(is_used, nums, result, results)
        return results


def main():
    nums = [1, 2, 3]
    print(Solution().permute(nums))


if __name__ == '__main__':
    main()