class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        if n == 1 and nums[0] != 1:
            return 1
        if n == 1 and nums[0] == 1:
            return 2

        i = 0
        while i < n:
            if nums[i] <= 0 or nums[i] > n or nums[i] == i + 1:
                i += 1
                continue

            target_index = nums[i] - 1
            if nums[target_index] == target_index + 1:
                i += 1
                continue
            nums[i] = nums[target_index]
            nums[target_index] = target_index + 1

        i = 0
        while i < n:
            if nums[i] == i + 1:
                i += 1
            else:
                break
        if i == n:
            return n + 1
        else:
            return i + 1


if __name__ == '__main__':
    x = [1, 1]
    print(Solution().firstMissingPositive(x))
