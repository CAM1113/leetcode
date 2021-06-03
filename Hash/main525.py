from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums = 0
        index_dic = {}
        index_dic[0] = -1
        max_length = 0
        for index, val in enumerate(nums):
            if val == 0:
                sums -= 1
            else:
                sums += 1
            if sums in index_dic.keys():
                if max_length < index - index_dic[sums]:
                    max_length = index - index_dic[sums]
            else:
                index_dic[sums] = index
        return max_length

if __name__ == '__main__':
    z = [0,0,1,0,0,0,1,1]
    print(Solution().findMaxLength(z))
