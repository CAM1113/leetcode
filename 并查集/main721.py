from typing import List


def find(array, index):
    if array[index] == index:
        return index
    root = find(array, array[index])
    array[index] = root
    return root


def union(array, index1, index2):
    array[find(array, index1)] = find(array, index2)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        array = [i for i in range(len(accounts))]
        for i in range(len(accounts)):
            for j in range(i + 1, len(accounts)):
                if accounts[i][0] != accounts[j][0]:
                    continue
                if find(array, i) == find(array, j):
                    continue
                for k in range(1, len(accounts[i])):
                    ac = accounts[i][k]
                    if ac in accounts[j]:
                        union(array, i, j)
                        break

        name_dic = {}
        acc_dic = {}
        for i in range(len(array)):
            root = find(array, i)
            if root in name_dic.keys():
                for index in range(1, len(accounts[i])):
                    acc_dic[root].add(accounts[i][index])
            else:
                name_dic[root] = accounts[i][0]
                acc_dic[root] = set(accounts[i][1:])
        result = []
        for k in name_dic.keys():
            acc = list(acc_dic[k])
            acc.sort()
            re = [name_dic[k],*acc]
            result.append(re)
        return result


def main():
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    print(Solution().accountsMerge(accounts))


if __name__ == '__main__':
    main()
