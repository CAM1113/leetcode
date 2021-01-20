from typing import List


def get_next_xy(index_x, index_y, index_d, array, n):
    if (index_x == 0 and index_d == 3) or (index_x == n - 1 and index_d == 1) \
            or (index_y == 0 and index_d == 2) or (index_y == n - 1 and index_d == 0):
        index_d = (index_d + 1) % 4
    else:
        if index_d == 0:
            new_index_x = index_x
            new_index_y = index_y + 1
        elif index_d == 1:
            new_index_x = index_x + 1
            new_index_y = index_y
        elif index_d == 2:
            new_index_x = index_x
            new_index_y = index_y - 1
        else:
            new_index_x = index_x - 1
            new_index_y = index_y
        if array[new_index_x][new_index_y] != -1:
            index_d = (index_d + 1) % 4

    if index_d == 0:
        new_index_x = index_x
        new_index_y = index_y + 1
    elif index_d == 1:
        new_index_x = index_x + 1
        new_index_y = index_y
    elif index_d == 2:
        new_index_x = index_x
        new_index_y = index_y - 1
    else:
        new_index_x = index_x - 1
        new_index_y = index_y
    return new_index_x, new_index_y,index_d


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        array = [[-1 for _ in range(n)] for _ in range(n)]
        index_x = 0
        index_y = 0
        index_d = 0
        for i in range(1,n * n +1):
            array[index_x][index_y] = i
            index_x, index_y,index_d = get_next_xy(index_x, index_y, index_d, array, n)

        return array


def main():
    print(Solution().generateMatrix(3))


if __name__ == '__main__':
    main()
