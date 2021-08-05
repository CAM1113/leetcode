import collections
from typing import List


def binary_search(arr: List[int], val: int):
    if len(arr) == 0:
        return 0
    if arr[0] >= val:
        return 0
    start = 0
    end = len(arr) - 1
    while start < end - 1:
        middle = (start + end) // 2
        if arr[middle] < val:
            start = middle
        else:
            end = middle
    return end


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        char_index_dic = {}
        index = 0
        for t in target:
            char_index_dic[t] = index
            index += 1
        seq = []
        for a in arr:
            if a in char_index_dic.keys():
                seq.append(char_index_dic[a])
        arr = seq
        if len(arr) == 0:
            return len(target)
        stack = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] == stack[-1]:
                continue
            if arr[i] > stack[-1]:
                stack.append(arr[i])
                continue
            index = binary_search(stack, arr[i])
            stack[index] = arr[i]
        return len(target) - len(stack)


if __name__ == '__main__':
    print(Solution().minOperations(target=[20, 9, 1, 3]
                                   , arr=[20, 1, 3, 9]))
