from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        index = 0
        result = []
        n = len(nums)
        while index < n:
            nums[(nums[index] - 1) % n] += n
            index += 1
        index = 0
        while index < n:
            if nums[index] <= n:
                result.append(index + 1)
            index += 1
        return result


if __name__ == '__main__':
    x = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(x))
