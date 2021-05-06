from typing import List

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        num_prior = [0] * numCourses
        prior_zero_list = deque()
        for arc in prerequisites:
            num_prior[arc[0]] += 1
        for index, val in enumerate(num_prior):
            if val == 0:
                prior_zero_list.appendleft(index)
        while len(prior_zero_list) != 0:
            index = prior_zero_list.popleft()
            # 移除弧
            arc_index = 0
            while arc_index < len(prerequisites):
                if prerequisites[arc_index][1] == index:
                    num_prior[prerequisites[arc_index][0]] -= 1
                    if num_prior[prerequisites[arc_index][0]] == 0:
                        prior_zero_list.append(prerequisites[arc_index][0])
                    prerequisites.pop(arc_index)
                else:
                    arc_index += 1
        return len(prerequisites) == 0


def main():
    n = 3
    p = [[1, 0], [2, 1]]
    print(Solution().canFinish(n, p))


if __name__ == '__main__':
    main()
