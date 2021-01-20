from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = 0
        ret = 0
        sum_dict = {0:1}
        for i in nums:
            sums += i
            if sum_dict.get(sums-k) is not None:
                ret += sum_dict[sums - k]
            if sum_dict.get(sums) is None:
                sum_dict[sums] = 1
            else:
                sum_dict[sums] += 1


        return ret


def main():
    nums = [-1,-1,1]
    k = 0
    print(Solution().subarraySum(nums, k))


if __name__ == '__main__':
    main()
