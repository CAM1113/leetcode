from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt_dic = {}
        max_cnt = 1
        for index, val in enumerate(nums):
            if val in cnt_dic.keys():
                val_info = cnt_dic[val]
                val_info[0] += 1
                val_info[2] = index
                if val_info[0] > max_cnt:
                    max_cnt = val_info[0]
            else:
                cnt_dic[val] = [1, index, index]

        min_len = len(nums)
        for val in cnt_dic.values():
            if val[0] == max_cnt and val[2] - val[1] < min_len:
                min_len = val[2] - val[1]
        return min_len + 1


if __name__ == '__main__':
    x = [1, 2, 2, 3, 1, 4, 2]
    print(Solution().findShortestSubArray(x))
