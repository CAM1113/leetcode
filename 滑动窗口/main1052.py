from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        start = 0
        end = 0
        used_index = -1
        is_used = False
        max_cus = 0
        cus_sum = 0
        zero_get = 0

        while end < len(customers):
            if grumpy[end] == 0:
                zero_get += customers[end]
                end += 1
                continue

            if is_used and used_index + X > end:
                cus_sum += customers[end]
                end += 1
                if cus_sum > max_cus:
                    max_cus = cus_sum
                continue
            if not is_used:
                is_used = True
                used_index = end
                continue
            if is_used and used_index + X <= end:
                while grumpy[start] == 0:
                    start += 1
                cus_sum -= customers[start]
                start += 1
                i = start
                while i <= end:
                    if grumpy[i] == 1:
                        used_index = i
                        is_used = True
                        break
                    i += 1
        return max_cus + zero_get


if __name__ == '__main__':
    c = [1,0,1,2,1,1,7,5]
    g=[0,1,0,1,0,1,0,1]
    x = 3
    print(Solution().maxSatisfied(c, g, x))
