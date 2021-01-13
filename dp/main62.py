# 超时
# def get_path(start_x, start_y, m, n, nums):
#     if start_x == m and start_y == n:
#         nums[0] += 1
#         return
#
#     if start_x < m:
#         get_path(start_x + 1, start_y, m, n, nums)
#
#     if start_y < n:
#         get_path(start_x, start_y + 1, m, n, nums)
#
#
# class Solution:
#
#     def uniquePaths(self, m: int, n: int) -> int:
#         nums = [0]
#         get_path(1, 1, m, n, nums)
#         return nums[0]

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
# 问总共有多少条不同的路径？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 动态规划
# 走向第i,j位置的路线数 = 走向第i-1,j位置的路线数 + 走向第i,j-1位置的路线数
# dp[i][j] = dp[i-1][j] + dp[i][j-1]
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        nums = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    nums[i][j] = 1
                else:
                    nums[i][j] = nums[i - 1][j] + nums[i][j - 1]
        return nums[m - 1][n - 1]


def main():
    m = 23
    n = 12
    print(Solution().uniquePaths(m, n))


if __name__ == '__main__':
    main()
