def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n - 1
        while start < end - 1:
            middle = (start + end) // 2
            if isBadVersion(middle):
                start = middle
            else:
                end = middle
        return start
