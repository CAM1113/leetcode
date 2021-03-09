import collections
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda xx: xx[0])
        index = 1
        max_num = 0
        num_index_dic = collections.defaultdict(list)
        num_index_dic[0] = [0]
        nums_list = [0]
        while index < n:
            is_over = False
            for k in nums_list:
                vs = num_index_dic[k]
                for v in vs:
                    if envelopes[v][0] < envelopes[index][0] and envelopes[v][1] < envelopes[index][1]:
                        num_index_dic[k + 1].append(index)
                        if k + 1 > max_num:
                            max_num += 1
                        is_over = True
                        if len(num_index_dic[k + 1]) == 1:
                            nums_list.append(k + 1)
                            nums_list.sort(reverse=True)
                        break
                if is_over:
                    break
            if not is_over:
                num_index_dic[0].append(index)

            index += 1
        return max_num + 1


if __name__ == '__main__':
    x = [[46, 89], [50, 53], [52, 68], [72, 45], [77, 81]]
    print(Solution().maxEnvelopes(x))
