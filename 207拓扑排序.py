from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        num_prior = [0 for _ in range(numCourses)]
        is_used = [False for _ in range(numCourses)]
        for arc in prerequisites:
            num_prior[arc[0]] += 1
        while sum(num_prior) != 0:
            index = 0
            while True:
                if index == len(num_prior):
                    return False
                if num_prior[index] == 0 and is_used[index] == False:
                    break
                index += 1
            is_used[index] = True
            arc_index = 0
            while arc_index < len(prerequisites):
                if prerequisites[arc_index][1] == index:
                    num_prior[prerequisites[arc_index][0]] -= 1
                    prerequisites.pop(arc_index)

                else:
                    arc_index += 1
        return True




def main():
    n = 3
    p = [[1, 0],[2,1]]
    print(Solution().canFinish(n, p))


if __name__ == '__main__':
    main()

