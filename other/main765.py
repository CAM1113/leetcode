from typing import List


def find_another(cp1):
    if cp1 % 2 == 0:
        return cp1 + 1
    else:
        return cp1 - 1


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        num_idx_dic = {}
        for index, val in enumerate(row):
            num_idx_dic[val] = index
        index = 0
        cnt = 0
        while index < len(row) - 1:
            cp1 = row[index]
            cp2 = find_another(cp1)
            cp2_index = num_idx_dic[cp2]
            if cp2_index == index + 1:
                index += 2
                continue
            cnt += 1
            num_idx_dic[row[index + 1]] = cp2_index
            index += 2
        return cnt


if __name__ == '__main__':
    r = [0, 2, 3, 1]
    print(Solution().minSwapsCouples(r))
