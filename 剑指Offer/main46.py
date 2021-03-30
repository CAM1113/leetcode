def dfs(nums, index, cnt):
    if index >= len(nums):
        cnt[0] += 1
        return
    for i in range(index + 1, index + 3):
        if i > len(nums):
            continue
        if int(nums[index: i]) < 26:
            if i - index >= 2 and nums[index] == '0':
                continue
            dfs(nums, i, cnt)


class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1
        cnt = [0]
        dfs(str(num), 0, cnt)
        return cnt[0]


if __name__ == '__main__':
    x = 506
    print(Solution().translateNum(x))
