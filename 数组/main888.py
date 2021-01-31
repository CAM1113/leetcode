from typing import List


def binary_search(b, target):
    start = 0
    end = len(b) - 1
    while start < end - 1:
        middle = (start + end) // 2
        if b[middle] >= target:
            end = middle
        else:
            start = middle
    if b[start] == target:
        return start
    if b[end] == target:
        return end
    return -1


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a_sum = sum(A)
        b_sum = sum(B)
        B.sort()
        A = set(A)
        for i in A:
            target = (b_sum + i - a_sum + i) / 2
            index = binary_search(B, target)
            if index != -1:
                return [i, B[index]]


def main():
    A = [1, 1]
    B = [2, 2]
    print(Solution().fairCandySwap(A, B))


if __name__ == '__main__':
    main()
