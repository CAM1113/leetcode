from typing import List


class Solution:

    def find(self, array, index):
        if array[index] == index:
            return index

        root = self.find(array, array[index])
        array[index] = root
        return root

    def union(self, array, index1, index2):
        root1 = self.find(array, index1)
        root2 = self.find(array, index2)
        array[root2] = root1

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        if len(s) <= 1 or len(pairs) == 0:
            return s
        s = list(s)
        # 创建并查集
        union_find = [i for i in range(len(s))]
        for p in pairs:
            self.union(union_find, p[0], p[1])

        # 根据并查集提取每个集合的元素
        uf_dict = {}
        for index in range(len(union_find)):
            root = self.find(union_find, index)
            if root in uf_dict:
                uf_dict[root].append(index)
            else:
                uf_dict[root] = [index]

        # 提取每个集合的字符，排序
        index_list = []
        val_list = []
        for k in uf_dict.keys():
            index_list.append(uf_dict[k])
            val = []
            for i in uf_dict[k]:
                val.append(s[i])
            val.sort()
            val_list.append(val)

        index = 0
        s = []
        while len(index_list) != 0:
            for i, l in enumerate(index_list):
                if l[0] == index:
                    s.append(val_list[i][0])
                    l.pop(0)
                    val_list[i].pop(0)
                    if len(l) == 0:
                        index_list.pop(i)
                        val_list.pop(i)
                    break
            index += 1
        return ''.join(s)


def main():
    s = "pwqlmqm"

    pairs = [[5, 3], [3, 0], [5, 1], [1, 1], [1, 5], [3, 0], [0, 2]]

    print(Solution().smallestStringWithSwaps(s, pairs))


if __name__ == '__main__':
    main()
