# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass


class Solution:
    def findCelebrity(self, n: int) -> int:
        in_degree = [0 for _ in range(n)]
        out_degree = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j):
                    in_degree[j] += 1
                    out_degree[i] += 1
        for i in range(n):
            if in_degree[i] == n - 1 and out_degree == 0:
                return i
        return -1
