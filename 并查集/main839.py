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


def is_true(str1, str2):
    if len(str1) != len(str2):
        return False
    num = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            num += 1
            if num > 2:
                return False
    return True


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        array = [i for i in range(len(strs))]
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if find(array, i) == find(array, j):
                    continue
                if is_true(strs[i], strs[j]):
                    union(array, i, j)
        root_set = set()
        for i in range(len(array)):
            root = find(array, i)
            root_set.add(root)
        return len(root_set)


def main():
    strs = ["tars", "rats", "arts", "star"]
    print(Solution().numSimilarGroups(strs))


if __name__ == '__main__':
    main()
