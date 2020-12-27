class Solution:
    def searchRange(self, nums, target: int):
        result = [-1, -1]
        for idx, n in enumerate(nums):
            if n == target:
                if result[0] == -1:
                    result[0] = idx
                    result[1] = idx
                else:
                    result[1] = idx
        return result
