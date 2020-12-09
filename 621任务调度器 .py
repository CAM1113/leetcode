from typing import List


class Solution:
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)
        count = {}
        for t in tasks:
            if count.get(t) is None:
                count[t] = 1
            else:
                count[t] = count[t] + 1
        count = list(count.values())
        count.sort()
        count = count[::-1]
        max_count = 0
        for item in count:
            if item == count[0]:
                max_count += 1
            else:
                break

        return max((count[0] - 1) * (n + 1) + max_count, len(tasks))


def main():
    tasks = ["A","A","A","B","B","B"]
    n = 2

    print(Solution().leastInterval(tasks, n))


if __name__ == '__main__':
    main()
