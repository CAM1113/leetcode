from sys import maxsize


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        min_length = maxsize
        close_result = maxsize
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            if nums[i] - target > min_length:
                break

            while j < k:
                sumed = nums[i] + nums[j] + nums[k]
                length = abs(sumed - target)
                if length < min_length:
                    min_length = length
                    close_result = sumed
                if sumed == target:
                    break
                if sumed < target:
                    j += 1
                if sumed > target:
                    k -= 1
            if min_length == 0:
                break

        return close_result


if __name__ == '__main__':
    nums = [0, 1, 2]
    target = 3
    print(Solution().threeSumClosest(nums, target))
