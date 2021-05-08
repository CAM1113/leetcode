from typing import List


def dfs(jobs: List[int], index: int, limit: int, current_time: List[int]):
    if index >= len(jobs):
        return True
    for i in range(len(current_time)):
        if current_time[i] + jobs[index] > limit:
            continue
        if i > 0 and current_time[i - 1] == 0:
            return False
        current_time[i] += jobs[index]
        if dfs(jobs, index + 1, limit, current_time):
            return True
        else:
            current_time[i] -= jobs[index]
    return False


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        start = min(jobs)
        end = sum(jobs)
        while start + 1 < end:
            middle = (start + end) // 2
            current_times = [0] * k
            if dfs(jobs, 0, middle, current_times):
                end = middle
            else:
                start = middle
        return end


def main():
    jobs = [1,2,4,7,8]
    k = 2
    print(Solution().minimumTimeRequired(jobs, k))


if __name__ == '__main__':
    main()
