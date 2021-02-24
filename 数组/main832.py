from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[int(not x) for x in line[::-1]] for line in A]


if __name__ == '__main__':
    x = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(Solution().flipAndInvertImage(x))
