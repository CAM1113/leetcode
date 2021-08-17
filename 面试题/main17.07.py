from typing import List


def find(array, index):
    if array[index] == index:
        return index
    root = find(array, array[index])
    array[index] = root
    return root


# def union(array, index1, index2):
#     root1 = find(array, index1)
#     root2 = find(array, index2)
#     array[root1] = root2


def union(array, name1, name2, name_index, people_nums, index_name):
    if name1 == name2:
        print("name1 == name2")
        return
    if name1 not in name_index.keys():
        index = len(name_index.keys())
        array.append(index)
        name_index[name1] = index
        index_name[index] = name1
        people_nums[name1] = 0

    if name2 not in name_index.keys():
        index = len(name_index.keys())
        array.append(index)
        name_index[name2] = index
        index_name[index] = name2
        people_nums[name2] = 0

    index1 = name_index[name1]
    index2 = name_index[name2]
    root1 = find(array, index1)
    root2 = find(array, index2)
    if root1 == root2:
        print("already union")
        return
    name1 = index_name[index1]
    name2 = index_name[index2]
    if name1 < name2:
        array[root2] = root1
        people_nums[name1] += people_nums[name2]
    else:
        array[root1] = root2
        people_nums[name2] += people_nums[name1]


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        name_index = {}
        index_name = {}
        people_nums = {}
        for index, n in enumerate(names):
            nn = n.split("(")
            name_index[nn[0]] = index
            index_name[index] = nn[0]
            people_nums[nn[0]] = int(nn[1][:-1])

        array = [i for i in range(len(name_index.keys()))]
        for s in synonyms:
            ss = s.split(",")
            n1 = ss[0][1:]
            n2 = ss[1][:-1]
            union(array, n1, n2, name_index, people_nums, index_name)

        result = {}
        for name in name_index.keys():
            index = name_index[name]
            root = find(array, index)
            if root == index:
                name = index_name[root]
                result[name] = people_nums[name]
        re = []
        for k in result.keys():
            re.append(f"{k}({result[k]})")
        return re


if __name__ == '__main__':
    print(Solution().trulyMostPopular(
        ["Kri(71)", "Kgabb(80)", "Tuvzkd(85)"],
        ["(Kri,Tuvzkd)", "(Kgabb,Tuvzkd)"]))
