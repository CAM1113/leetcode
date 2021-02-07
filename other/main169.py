from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dic = {}
        for n in nums:
            if n in count_dic.keys():
                count_dic[n] += 1
            else:
                count_dic[n] = 1
            if count_dic[n] > len(nums) // 2:
                return count_dic[n]
