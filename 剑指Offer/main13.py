def get_bit_sum(n):
    nums = 0
    while n > 0:
        nums += n % 10
        n //= 10
    return nums


def dfs(m, n, current_x, current_y, is_used, cnt, num_bit_sum_dict, k):
    if m < 1 or n < 1:
        return 0
    cnt[0] += 1
    is_used[current_x][current_y] = True
    if current_x > 0 and not is_used[current_x - 1][current_y] and \
            num_bit_sum_dict[current_x - 1] + num_bit_sum_dict[current_y] <= k:
        dfs(m, n, current_x - 1, current_y, is_used, cnt, num_bit_sum_dict, k)
    if current_x < m - 1 and (not is_used[current_x + 1][current_y]) and \
            num_bit_sum_dict[current_x + 1] + num_bit_sum_dict[current_y] <= k:
        dfs(m, n, current_x + 1, current_y, is_used, cnt, num_bit_sum_dict, k)

    if current_y > 0 and not is_used[current_x][current_y - 1] and \
            num_bit_sum_dict[current_x] + num_bit_sum_dict[current_y - 1] <= k:
        dfs(m, n, current_x, current_y - 1, is_used, cnt, num_bit_sum_dict, k)

    if current_y < n - 1 and not is_used[current_x][current_y + 1] and \
            num_bit_sum_dict[current_x] + num_bit_sum_dict[current_y + 1] <= k:
        dfs(m, n, current_x, current_y + 1, is_used, cnt, num_bit_sum_dict, k)


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        num_bit_sum_dict = {}
        for i in range(max(m, n)):
            num_bit_sum_dict[i] = get_bit_sum(i)
        cnt = [0]
        is_used = [[False for _ in range(n)] for _ in range(m)]
        dfs(m, n, 0, 0, is_used, cnt, num_bit_sum_dict, k)

        return cnt[0]


if __name__ == '__main__':
    m = 1
    n = 2
    k = 1
    print(Solution().movingCount(m, n, k))
