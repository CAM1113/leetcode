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
    def equationsPossible(self, equations: List[str]) -> bool:
        array = [i for i in range(26)]
        neq = []
        for eq in equations:
            if eq[1] == '!':
                neq.append(eq)
                continue
            union(array, ord(eq[0]) - 97, ord(eq[-1]) - 97)
        for n in neq:
            root1 = find(array, ord(n[0]) - 97)
            root2 = find(array, ord(n[-1]) - 97)
            if root1 == root2:
                return False
        return True


if __name__ == '__main__':
    x = ["a==b", "b==c", "a!=c"]
    print(Solution().equationsPossible(x))
