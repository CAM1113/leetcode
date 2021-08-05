from cmath import log
from math import log2
from typing import List


def change_index(num):
    line = int(log2(num))
    if line % 2 == 0:
        return num
    num_lin = 2 ** line
    end = num_lin
    start = end * 2 - 1
    return start - (num - end)


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        index = change_index(label)
        result = [index]
        while result[-1] != 1:
            result.append(result[-1] // 2)
        result = result[::-1]
        return [change_index(a) for a in result]

if __name__ == '__main__':
    labels = 3
    print(Solution().pathInZigZagTree(labels))
