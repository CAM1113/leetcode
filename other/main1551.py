class Solution:
    def minOperations(self, n: int) -> int:
        i = 1
        time = 0
        while i < n:
            if i >= n:
                break
            time += n - i
            i += 2
        return time
