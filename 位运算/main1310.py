from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        xor = 0
        for n in arr:
            xor ^= n
            prefix_xor.append(xor)
        result = []
        for q in queries:
            result.append(prefix_xor[q[1]+1] ^ prefix_xor[q[0]])
        return result


if __name__ == '__main__':
    ar = [1, 3, 4, 8]
    querie = [[0, 1], [1, 2], [0, 3], [3, 3]]
    print(Solution().xorQueries(ar, querie))
