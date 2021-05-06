from typing import List


def get_days(weights: List[int], W: int):
    days = 0
    sum_w = 0
    for w in weights:
        sum_w += w
        if sum_w > W:
            days += 1
            sum_w = w
    if sum_w > 0:
        days += 1
    return days


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        max_weight = sum(weights)
        min_weight = max(weights)
        if get_days(weights, min_weight) <= D:
            return min_weight
        while min_weight < max_weight - 1:
            middle = (min_weight + max_weight) // 2
            days = get_days(weights, middle)
            if days > D:
                min_weight = middle
            else:
                max_weight = middle
        return max_weight


if __name__ == '__main__':
    weights = [1, 2, 3, 1, 1]
    d = 4
    print(Solution().shipWithinDays(weights, d))
