import collections
from typing import List


def find(array, index):
    if array[index] == index:
        return index
    root = find(array, array[index])
    array[index] = root
    return root


def union(array, index1, index2):
    root1 = find(array, index1)
    root2 = find(array, index2)
    array[root2] = root1


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        array = [i for i in range(len(source))]
        for index in allowedSwaps:
            union(array, index[0], index[1])

        root_dic = collections.defaultdict(list)
        for i in range(len(array)):
            root = find(array, i)
            root_dic[root].append(i)
        result = 0
        for v in root_dic.values():
            s = [source[i] for i in v]
            t = [target[i] for i in v]
            t = collections.Counter(t)
            for c in s:
                if c in t.keys():
                    if t[c] == 0:
                        result += 1
                    else:
                        t[c] -= 1
                else:
                    result += 1

        return result


if __name__ == '__main__':
    source = [2, 3, 1]

    target = [1, 2, 2]

    allowedSwaps = [[0, 2], [1, 2]]

    print(Solution().minimumHammingDistance(source, target, allowedSwaps))
