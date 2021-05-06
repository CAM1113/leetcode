class Solution:
    def minCostClimbingStairs(self, total_cost) -> int:
        for i in range(2, len(total_cost)):
            total_cost[i] = min(total_cost[i - 1] + total_cost[i], total_cost[i - 2] + total_cost[i])
        return total_cost[-1]


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(Solution().minCostClimbingStairs(cost))
