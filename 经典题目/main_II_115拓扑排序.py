import collections
from typing import List


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        if len(seqs) == 0:
            return False
        backward_node = collections.defaultdict(set)
        num_in_degree = collections.defaultdict(set)

        for seq in seqs:
            index = len(seq) - 2
            while index >= 0:
                backward_node[seq[index]].add(seq[index + 1])
                num_in_degree[seq[index + 1]].add(seq[index])
                index -= 1
            if len(num_in_degree[seq[0]]) == 0:
                continue
        if org[0] not in num_in_degree.keys():
            return False
        if len(num_in_degree[org[0]]) != 0:
            return False
        if len(num_in_degree.keys()) > len(seqs):
            return False

        stack = [org[0]]
        index = 0
        while len(stack) > 0:
            n = stack[0]
            stack.pop()
            if n != org[index]:
                return False
            index += 1
            if index >= len(org):
                return True
            for node in backward_node[n]:
                num_in_degree[node].remove(n)
                if len(num_in_degree[node]) == 0:
                    stack.append(node)
            if len(stack) != 1:
                return False
        return True


if __name__ == '__main__':
    print(Solution().sequenceReconstruction([5, 3, 2, 4, 1],
                                            [[5, 3, 2, 4], [4, 1], [1], [3], [2, 4], [1000000000]]))
