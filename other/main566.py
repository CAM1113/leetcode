from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
        res = []
        num = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if num % c == 0:
                    res.append([])
                num += 1
                res[-1].append(nums[i][j])
        return res


if __name__ == '__main__':
    x = [[1, 2, 5],
         [3, 4, 6]]
    rr = 3
    cc = 2
    print(Solution().matrixReshape(x, rr, cc))
