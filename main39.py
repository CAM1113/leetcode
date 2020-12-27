def dfs(nums, start_index, target, result, results):
    result.append(nums[start_index])
    if sum(result) == target:
        results.append(result[:])
        return
    if sum(result) > target:
        return
    if sum(result) < target:
        for i in range(start_index, len(nums)):
            if sum(result) + nums[i] > target:
                break
            dfs(nums, i, target, result, results)
            result.pop()


class Solution:
    def combinationSum(self, candidates, target: int):
        candidates.sort()
        results = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            dfs(nums=candidates, start_index=i, target=target, result=[], results=results)
        return results


def main():
    candidates = [2, 3, 5]
    target = 8
    print(Solution().combinationSum(candidates, target))


if __name__ == '__main__':
    main()
