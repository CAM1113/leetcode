from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum = [0 for _ in range(n + 1)]
        for b in bookings:
            start, end, val = b[0], b[1], b[2]
            prefix_sum[start] += val
            if end < n:
                prefix_sum[end + 1] -= val
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]
        return prefix_sum[1:]
