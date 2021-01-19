from typing import List


def is_ok(cost, start_index):
    num = len(cost)
    val = 0
    for i in range(num):
        index = (i + start_index) % num
        val += cost[index]
        if val < 0:
            return False
    return True


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            if gas[0] < cost[0]:
                return -1
            else:
                return 0
        for i in range(len(gas)):
            cost[i] = gas[i] - cost[i]
        for i in range(len(cost)):
            if cost[i] < 0:
                continue
            if cost[i] > 0 and cost[i - 1] > 0:
                continue
            if is_ok(cost, i):
                return i
        return -1


def main():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(Solution().canCompleteCircuit(gas, cost))


if __name__ == '__main__':
    main()
