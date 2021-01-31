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
    def removeStones(self, stones: List[List[int]]) -> int:
        element_dic = {}
        array = [i for i in range(len(stones))]
        for index, s in enumerate(stones):
            if s[0] in element_dic.keys():
                root = find(array, element_dic[s[0]])
                i = find(array, index)
                union(array, root, i)
            if s[1] + 10000 in element_dic.keys():
                root = find(array, element_dic[s[1]+10000])
                i = find(array, index)
                union(array, root, i)
            element_dic[s[0]] = find(array, index)
            element_dic[s[1] + 10000] = find(array, index)
        element_dic = set()
        for i in range(len(stones)):
            root = find(array, i)
            element_dic.add(root)
        return len(stones) - len(element_dic)


if __name__ == '__main__':
    s = [[0, 1], [1, 0], [1, 1]]
    print(Solution().removeStones(s))
